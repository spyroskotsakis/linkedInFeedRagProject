# Buck Build Tool | Selenium

**URL:** https://www.selenium.dev/documentation/legacy/developers/buck
**Word Count:** 240
**Links Count:** 205
**Scraped:** 2025-07-17 06:13:37
**Status:** completed

---

# Buck Build Tool

Buck is a build tool from Facebook that we were working with to replace Crazy fun. We have since replaced it with [Bazel](https://bazel.build/).

This documentation previously located [on the wiki](https://github.com/SeleniumHQ/selenium/wiki/Buck)   You can read the documentation for the legacy [Crazy Fun Build tool](https://www.selenium.dev/documentation/legacy/developers/crazy_fun_build/).

## Building Selenium with Buck

The easiest thing to do is to just run “./go”. The build process will download the right version of Buck for you so long as there’s no `.nobuckcheck` file in the root of the project. The download ends up in `buck-out/crazy-fun/HASH/buck.pex` where `HASH` is the value of the current buck version \(given in the `.buckversion` file in the root of the project.

If you’d like to build and run our fork of Buck, then:               git clone https://github.com/SeleniumHQ/buck.git     cd buck && ant     export PATH=`pwd`/bin:$PATH     cd ~/src/selenium      buck build chrome firefox htmlunit remote leg-rc     buck test --all     

## Updating the `buck.pex`

Should you need to update the version of Buck that is downloaded:

  * Checkout the source to Buck and build the PEX: `buck build --show-output buck`   * Figure out the git hash of the version you’ve just built. Normally that’ll be the HEAD of master. Put that full hash into the `.buckversion` of the main selenium project.   * Put the md5 hash of the PEX into the `.buckhash` file in the main selenium project.   * Create a new release of SeleniumHQ’s Buck fork on GitHub. The name is `buck-release-$VERSION`, where $VERSION is whatever’s in `.buckversion` in the main selenium project.   * Upload the PEX to the release, and make the release public.   * Commit the changes to the main selenium project and push them.

Last modified January 10, 2022: [More wiki \(\#907\) \[deploy site\] \(adcf706a1ad\)](https://github.com/SeleniumHQ/seleniumhq.github.io/commit/adcf706a1ad907d028dc57d10201a265972432af)