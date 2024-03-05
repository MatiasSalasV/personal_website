call .venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
reflex init
reflex export --frontend-only
rmdir /s /q .\public
powershell -Command "Expand-Archive -LiteralPath frontend.zip -DestinationPath .\public"
del frontend.zip
deactivate


