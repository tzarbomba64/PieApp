# PieApp GitHub Repo Files

Place these files at the **root** of your `tzarbomba64/PieApp` repository.

## Files

- `PieApp.ipa`  
  Upload your signed PieApp IPA here.

- `manifest.plist`  
  Points to the raw IPA for OTA install.

- `install.html`  
  Kicks off OTA installation when opened in Safari.

- `packager.py`  
  Flask endpoint at `/packager` that packages IPA and manifest into a ZIP.

- `requirements.txt`  
  Lists `flask` and `requests` for the packager.

## Deployment

1. Commit all files above to the **root** of the `main` branch.
2. Enable GitHub Pages: **Settings → Pages → Source: main branch (root)**
3. Access Installer:  
   ```
   https://tzarbomba64.github.io/PieApp/install.html
   ```
4. (Optional) To get a ZIP of the IPA+manifest, run `packager.py` on your server (e.g., Replit) and visit:
   ```
   https://<your-server>/packager
   ```

Now, anyone opening `install.html` in Safari on iPhone will install PieApp OTA!
