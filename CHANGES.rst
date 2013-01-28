Changelog
=========

Version 0.4.2
-------------

    * Re-upload of the package, previous build didn't include images.

Version 0.4.1
-------------

    * Fixed a bug in the adapter that caused the icon path to be wrongly
      escaped. (#11)

Version 0.4
-----------

    * Fallback to ``notify-send`` if the Python module is not available. Helpful
      for situations where you're inside a virtualenv.
    * Fixed plugin configuration.
    * Python 3 support.
