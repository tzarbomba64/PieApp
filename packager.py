#!/usr/bin/env python3
import os
import io
import zipfile
from flask import Flask, send_file, Response

app = Flask(__name__)

@app.route('/packager', methods=['GET'])
def packager():
    required_files = ['PieApp.ipa', 'manifest.plist']
    for fname in required_files:
        if not os.path.isfile(fname):
            return Response(f"Missing file: {fname}", status=404)

    memory_zip = io.BytesIO()
    with zipfile.ZipFile(memory_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for fname in required_files:
            zf.write(fname, arcname=fname)
    memory_zip.seek(0)
    return send_file(
        memory_zip,
        mimetype='application/zip',
        as_attachment=True,
        download_name='PieApp_Package.zip'
    )

if __name__ == '__main__':
    import os
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
