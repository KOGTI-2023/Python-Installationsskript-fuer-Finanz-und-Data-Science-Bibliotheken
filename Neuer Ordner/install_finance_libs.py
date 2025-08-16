import os
import subprocess
import sys
import shutil
import platform
import urllib.request
import re
import ctypes

# Liste der zu installierenden Bibliotheken, ohne TA-Lib
LIBRARIES = [
    'flask', 'matplotlib', 'numpy', 'pandas', 'scikit-learn',
    'scipy', 'seaborn', 'jupyter', 'yfinance', 'statsmodels',
    'openpyxl', 'mplfinance', 'requests', 'beautifulsoup4'
]

# Liste der unterstützten TA-Lib Wheel-Dateien (64-Bit-Versionen)
# Dies ist wichtig für die automatische Installation unter Windows
TA_LIB_URLS = {
    "3.8": "https://download.lfd.uci.edu/pythonlibs/p3.8/TA_Lib-0.4.24-cp38-cp38-win_amd64.whl",
    "3.9": "https://download.lfd.uci.edu/pythonlibs/p3.9/TA_Lib-0.4.24-cp39-cp39-win_amd64.whl",
    "3.10": "https://download.lfd.uci.edu/pythonlibs/p3.10/TA_Lib-0.4.24-cp310-cp310-win_amd64.whl",
    "3.11": "https://download.lfd.uci.edu/pythonlibs/p3.11/TA_Lib-0.4.24-cp311-cp311-win_amd64.whl",
    "3.12": "https://download.lfd.uci.edu/pythonlibs/p3.12/TA_Lib-0.4.24-cp312-cp312-win_amd64.whl"
}

def is_admin():
    """
    Überprüft, ob das Skript mit Administratorrechten ausgeführt wird.
    """
    try:
        return os.getuid() == 0
    except AttributeError:
        # Für Windows
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

def check_python_version():
    """
    Überprüft die Python-Version und das System-Architektur.
    """
    version = sys.version_info
    major, minor = version.major, version.minor
    print(f"Ihre Python-Version: {major}.{minor}")

    if not (major == 3 and minor >= 8):
        print("Fehler: Dieses Skript erfordert Python 3.8 oder neuer.")
        return None

    if platform.architecture()[0] != '64bit':
        print("Fehler: Dieses Skript erfordert ein 64-Bit-Python. Bitte installieren Sie die 64-Bit-Version.")
        return None
    
    return f"{major}.{minor}"

def install_ta_lib(pip_path, python_version):
    """
    Installiert TA-Lib mit einer passenden .whl-Datei für Windows.
    """
    if not (sys.platform == "win32" or sys.platform == "cygwin"):
        print("TA-Lib Installation wird nur für Windows unterstützt. Überspringe...")
        return True

    ta_lib_whl_url = TA_LIB_URLS.get(python_version)

    if not ta_lib_whl_url:
        print(f"Warnung: Keine passende TA-Lib-Version für Python {python_version} gefunden. TA-Lib wird nicht installiert.")
        return False

    whl_filename = os.path.basename(ta_lib_whl_url)
    whl_filepath = os.path.join(os.getcwd(), whl_filename)
    
    try:
        print(f"Versuche, TA-Lib von {ta_lib_whl_url} herunterzuladen...")
        urllib.request.urlretrieve(ta_lib_whl_url, whl_filepath)
        print("Herunterladen abgeschlossen.")
        
        print("Installiere TA-Lib...")
        subprocess.run([pip_path, 'install', whl_filepath], check=True)
        print("TA-Lib erfolgreich installiert.")
        return True
    except Exception as e:
        print(f"Fehler bei der TA-Lib-Installation: {e}")
        print("Versuche es mit 'pip install TA-Lib' (benötigt Build-Tools).")
        try:
            subprocess.run([pip_path, 'install', 'TA-Lib'], check=True)
            print("TA-Lib erfolgreich über pip installiert.")
            return True
        except Exception as e:
            print(f"Fehler: TA-Lib konnte nicht installiert werden. Bitte manuell installieren.")
            return False
    finally:
        if os.path.exists(whl_filepath):
            os.remove(whl_filepath)

def install_libraries(pip_path, python_version):
    """
    Installiert die Bibliotheken mithilfe des angegebenen pip-Pfads.
    """
    print("-" * 50)
    print("Starte die Installation der Python-Bibliotheken...")
    print(f"Verwendeter pip-Pfad: {pip_path}")
    print("-" * 50)

    # TA-Lib separat installieren
    ta_lib_success = install_ta_lib(pip_path, python_version)
    if not ta_lib_success:
        print("TA-Lib wurde nicht installiert. Fortsetzung mit anderen Bibliotheken.")

    # Andere Bibliotheken installieren
    for lib in LIBRARIES:
        try:
            print(f"Installiere {lib}...")
            subprocess.run([pip_path, 'install', lib], check=True)
            print(f"{lib} erfolgreich installiert.")
        except subprocess.CalledProcessError as e:
            print(f"Fehler beim Installieren von {lib}: {e}")
            print("Versuche es erneut...")
            try:
                subprocess.run([pip_path, 'install', lib], check=True)
                print(f"{lib} erfolgreich installiert.")
            except subprocess.CalledProcessError as e:
                print(f"Konnte {lib} nicht installieren. Bitte überprüfen Sie die Fehlermeldung.")
        except Exception as e:
            print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")

    print("-" * 50)
    print("Installation abgeschlossen.")

def create_venv():
    """
    Erstellt eine virtuelle Umgebung und gibt den pip-Pfad zurück.
    """
    print("\nErstelle eine virtuelle Umgebung...")
    venv_name = input("Geben Sie den Namen für die virtuelle Umgebung ein (Standard: .venv): ")
    if not venv_name:
        venv_name = ".venv"

    if os.path.exists(venv_name):
        shutil.rmtree(venv_name)
    
    try:
        subprocess.run([sys.executable, '-m', 'venv', venv_name], check=True)
        print(f"Virtuelle Umgebung '{venv_name}' erfolgreich erstellt.")
        
        if sys.platform == "win32" or sys.platform == "cygwin":
            pip_path = os.path.join(venv_name, 'Scripts', 'pip.exe')
        else:
            pip_path = os.path.join(venv_name, 'bin', 'pip')
            
        print(f"Um die virtuelle Umgebung zu aktivieren, führen Sie aus:")
        if sys.platform == "win32" or sys.platform == "cygwin":
            print(f"{venv_name}\\Scripts\\activate")
        else:
            print(f"source {venv_name}/bin/activate")
            
        return pip_path
    except Exception as e:
        print(f"Fehler beim Erstellen der virtuellen Umgebung: {e}")
        return None

def main():
    """
    Hauptfunktion des Skripts, die die Menüführung steuert.
    """
    print("=" * 50)
    print("Python Installationsskript für Finanz- & Data-Science-Bibliotheken")
    print("=" * 50)
    
    python_version = check_python_version()
    if not python_version:
        input("\nDrücken Sie eine Taste, um das Programm zu beenden...")
        return
        
    choice = input(
        "\nWählen Sie eine Installationsmethode:\n"
        "1. Global (Alle Benutzer)\n"
        "2. In einer virtuellen Umgebung (.venv)\n"
        "3. Beenden\n"
        "Ihre Wahl: "
    )
    
    if choice == '1':
        print("\nSie haben die globale Installation gewählt.")
        install_libraries(sys.executable.replace("python.exe", "pip.exe"), python_version)
    elif choice == '2':
        pip_path = create_venv()
        if pip_path:
            install_libraries(pip_path, python_version)
    elif choice == '3':
        print("Vorgang abgebrochen.")
    else:
        print("Ungültige Auswahl. Vorgang abgebrochen.")

    input("\nInstallation beendet. Drücken Sie eine Taste, um das Programm zu beenden...")

if __name__ == "__main__":
    main()
