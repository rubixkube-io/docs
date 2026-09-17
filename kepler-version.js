/*
 * Keeps the Kepler version on the install page current in the reader's browser.
 *
 * The page ships with a real version baked into <span id="kepler-version">, written
 * by scripts/update_kepler_version.py, so crawlers, LLMs and readers without
 * JavaScript always see a correct value. This script upgrades that text in place
 * when kepler-releases has published something newer than the last build.
 *
 * Mintlify loads every .js file in the content directory on every page, so this
 * does nothing unless the span is present. Mintlify also navigates as a single-page
 * app, which is why an observer re-checks after client-side route changes.
 */

(function () {
  "use strict";

  var ELEMENT_ID = "kepler-version";
  var API_URL =
    "https://api.github.com/repos/rubixkube-io/kepler-releases/releases/latest";
  var CACHE_KEY = "kepler-latest-version";
  // One lookup per browsing session. The unauthenticated GitHub API allows 60
  // requests per hour per IP, and a shared office address is one IP.
  var CACHE_TTL_MS = 30 * 60 * 1000;

  var inFlight = false;

  function readCache() {
    try {
      var raw = window.sessionStorage.getItem(CACHE_KEY);
      if (!raw) return null;
      var entry = JSON.parse(raw);
      if (!entry || typeof entry.version !== "string") return null;
      if (Date.now() - entry.at > CACHE_TTL_MS) return null;
      return entry.version;
    } catch (error) {
      // Private browsing and blocked site data both throw here.
      return null;
    }
  }

  function writeCache(version) {
    try {
      window.sessionStorage.setItem(
        CACHE_KEY,
        JSON.stringify({ version: version, at: Date.now() })
      );
    } catch (error) {
      /* Caching is an optimisation, not a requirement. */
    }
  }

  function apply(version) {
    if (!version) return;
    var target = document.getElementById(ELEMENT_ID);
    if (!target) return;
    if (target.textContent.trim() === version) return;
    target.textContent = version;
  }

  function fetchLatest() {
    if (inFlight) return;
    inFlight = true;

    fetch(API_URL, { headers: { Accept: "application/vnd.github+json" } })
      .then(function (response) {
        if (!response.ok) throw new Error("GitHub API " + response.status);
        return response.json();
      })
      .then(function (release) {
        if (release.draft || !release.tag_name) return;
        var version = String(release.tag_name).replace(/^v/, "");
        // Guard against anything that is not a plain version string before it
        // reaches the DOM.
        if (!/^[\w.+-]{1,40}$/.test(version)) return;
        writeCache(version);
        apply(version);
      })
      .catch(function () {
        // Rate limited, offline, or GitHub is down. The baked-in version stands.
      })
      .finally(function () {
        inFlight = false;
      });
  }

  function refresh() {
    if (!document.getElementById(ELEMENT_ID)) return;
    var cached = readCache();
    if (cached) {
      apply(cached);
      return;
    }
    fetchLatest();
  }

  refresh();

  // Mintlify swaps page content without a full load, so the span can appear
  // long after this script first ran.
  if (typeof MutationObserver === "function" && document.body) {
    var pending = null;
    new MutationObserver(function () {
      window.clearTimeout(pending);
      pending = window.setTimeout(refresh, 100);
    }).observe(document.body, { childList: true, subtree: true });
  }
})();
