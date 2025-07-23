# -*- coding: utf-8 -*-
import subprocess
import sys
import platform
import os
import glob
import re
import requests # Benötigt für den automatischen Download
from bs4 import BeautifulSoup # Benötigt für das Parsen der Webseite

def print_status(message, level="INFO"):
    """Gibt Statusmeldungen mit verschiedenen Ebenen aus."""
    if level == "INFO":
        print(f"[INFO] {message}")
    elif level == "WARNING":
        print(f"[WARNUNG] {message}")
    elif level == "ERROR":
        print(f"[FEHLER] {message}")
    elif level == "SUCCESS":
        print(f"[ERFOLG] {message}")

def check_python_version():
    """Prüft die installierte Python-Version und die Architektur."""
    print_status("Überprüfe Python-Version und Architektur...")
    python_version_str = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
    print_status(f"Erkannte Python-Version: {python_version_str}")

    if sys.version_info.major < 3 or (sys.version_info.major == 3 and sys.version_info.minor < 8):
        print_status(f"Ihre Python-Version ist {python_version_str}. "
                     "Dieses Skript erfordert Python 3.8 oder höher. Bitte aktualisieren Sie Ihre Python-Installation.", "ERROR")
        sys.exit(1)
    print_status(f"Python-Version {python_version_str} ist kompatibel.")

    if platform.architecture()[0] != '64bit':
        print_status("Dieses Skript ist für 64-Bit Windows 11 PCs konzipiert. Ihre Architektur ist nicht 64-Bit.", "WARNING")
        print_status("Dies könnte zu Problemen bei der Installation einiger Bibliotheken führen, insbesondere TA-Lib.", "WARNING")
    else:
        print_status("Architektur: 64-Bit (kompatibel).")

    return f"cp{sys.version_info.major}{sys.version_info.minor}", "win_amd64"

def install_package(package_name):
    """Installiert ein Python-Paket mit pip."""
    print_status(f"Versuche, '{package_name}' zu installieren...")
    try:
        # Verwende sys.executable, um sicherzustellen, dass der richtige Pip verwendet wird
        # --break-system-packages ist wichtig für globale Installationen in bestimmten Umgebungen
        result = subprocess.run([sys.executable, "-m", "pip", "install", package_name, "--break-system-packages"],
                                capture_output=True, text=True, check=True)
        print_status(f"'{package_name}' erfolgreich installiert.", "SUCCESS")
        # print(result.stdout) # Optional: Ausgabe von pip anzeigen
    except subprocess.CalledProcessError as e:
        print_status(f"Fehler bei der Installation von '{package_name}': {e.returncode}", "ERROR")
        print_status(f"Standardausgabe: {e.stdout}", "ERROR")
        print_status(f"Fehlerausgabe: {e.stderr}", "ERROR")
        print_status(f"Bitte versuchen Sie, '{package_name}' manuell über die Befehlszeile zu installieren: "
                     f"'{sys.executable} -m pip install {package_name} --break-system-packages'", "WARNING")
    except Exception as e:
        print_status(f"Ein unerwarteter Fehler ist aufgetreten bei der Installation von '{package_name}': {e}", "ERROR")

def download_ta_lib_whl(python_tag, arch_tag):
    """Versucht, die passende TA-Lib .whl-Datei von der Gohlke-Seite herunterzuladen."""
    url = "https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib"
    print_status(f"Versuche, TA-Lib .whl-Datei von {url} herunterzuladen...")
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Löst HTTPError für schlechte Antworten (4xx oder 5xx) aus
        soup = BeautifulSoup(response.content, 'html.parser')

        # Suche nach Links, die TA_Lib enthalten und zur Python-Version/Architektur passen
        # Beispiel: TA_Lib‑0.4.24‑cp39‑cp39‑win_amd64.whl
        pattern = re.compile(rf"TA_Lib-.*-{python_tag}-{python_tag}-{arch_tag}\.whl", re.IGNORECASE)
        
        found_link = None
        for link in soup.find_all('a', href=True):
            filename = link['href'].split('/')[-1] # Extrahiere Dateiname
            if pattern.match(filename):
                found_link = link['href']
                break

        if found_link:
            download_url = f"https://www.lfd.uci.edu/~gohlke/pythonlibs/{found_link}"
            local_filename = found_link.split('/')[-1]
            print_status(f"Gefundene TA-Lib-Datei: {local_filename}. Starte Download von {download_url}...")
            
            # Download der Datei
            file_response = requests.get(download_url, stream=True, timeout=30)
            file_response.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in file_response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print_status(f"'{local_filename}' erfolgreich heruntergeladen.", "SUCCESS")
            return local_filename
        else:
            print_status(f"Keine passende TA-Lib .whl-Datei für Python {python_tag} und {arch_tag} auf der Seite gefunden.", "WARNING")
            return None

    except requests.exceptions.RequestException as e:
        print_status(f"Fehler beim Zugriff auf die Download-Seite oder beim Herunterladen der Datei: {e}", "ERROR")
        print_status("Bitte überprüfen Sie Ihre Internetverbindung oder versuchen Sie den manuellen Download.", "WARNING")
        return None
    except Exception as e:
        print_status(f"Ein unerwarteter Fehler ist beim TA-Lib-Download aufgetreten: {e}", "ERROR")
        return None

def install_ta_lib(python_tag, arch_tag):
    """Versucht, TA-Lib zu installieren, vorzugsweise über eine heruntergeladene .whl-Datei."""
    print_status("Versuche, TA-Lib zu installieren. Dies kann auf Windows etwas knifflig sein.")
    
    # Zuerst versuchen, die .whl-Datei automatisch herunterzuladen
    ta_lib_whl_file = download_ta_lib_whl(python_tag, arch_tag)

    if ta_lib_whl_file and os.path.exists(ta_lib_whl_file):
        print_status(f"Gefundene und heruntergeladene TA-Lib .whl-Datei: '{ta_lib_whl_file}'. Versuche Installation...", "INFO")
        try:
            # --break-system-packages ist wichtig für globale Installationen
            subprocess.check_call([sys.executable, "-m", "pip", "install", ta_lib_whl_file, "--break-system-packages"])
            print_status("TA-Lib erfolgreich über .whl-Datei installiert.", "SUCCESS")
        except subprocess.CalledProcessError as e:
            print_status(f"Fehler bei der Installation von TA-Lib über .whl-Datei: {e}", "ERROR")
            print_status("Bitte überprüfen Sie, ob die .whl-Datei zur Python-Version und Architektur passt.", "WARNING")
            print_status("Versuchen Sie die manuelle Installation: "
                         f"'{sys.executable} -m pip install {ta_lib_whl_file} --break-system-packages'", "WARNING")
        except Exception as e:
            print_status(f"Ein unerwarteter Fehler ist aufgetreten bei der Installation von TA-Lib: {e}", "ERROR")
    else:
        print_status("Konnte TA-Lib .whl-Datei nicht automatisch herunterladen oder finden.", "WARNING")
        print_status("Versuche dennoch die direkte pip-Installation (dies schlägt oft fehl ohne Build-Tools wie Visual C++ Build Tools)...", "INFO")
        install_package("TA-Lib") # Versuch der direkten Installation

def main():
    """Hauptfunktion des Installationsskripts."""
    print_status("Starte das Installationsskript für Finanz- und Data-Science-Bibliotheken.")

    # Sicherstellen, dass pip selbst aktuell ist
    print_status("Aktualisiere pip...")
    install_package("pip --upgrade")

    # Installiere requests und beautifulsoup4 zuerst, da sie für den TA-Lib Download benötigt werden könnten
    print_status("\nInstalliere notwendige Pakete für den TA-Lib Download (requests, beautifulsoup4)...")
    install_package("requests")
    install_package("beautifulsoup4")

    python_tag, arch_tag = check_python_version()

    # Liste der zu installierenden Bibliotheken
    # TA-Lib wird separat behandelt
    packages = [
        "Flask",
        "matplotlib",
        "numpy",
        "pandas",
        "scikit-learn",  # Für Machine Learning
        "scipy",         # Für wissenschaftliches Rechnen
        "seaborn",       # Für statistische Datenvisualisierung
        "jupyter",       # Für interaktives Computing (Jupyter Notebook/Lab)
        "yfinance",      # Für Finanzdaten von Yahoo Finance
        "statsmodels",   # Für statistische Modellierung
        "openpyxl",      # Für das Lesen/Schreiben von Excel-Dateien (oft nützlich mit Pandas)
        "mplfinance",    # Für Finanzdiagramme (candlestick etc.)
    ]

    install_ta_lib(python_tag, arch_tag) # TA-Lib separat behandeln

    print_status("\nBeginne mit der Installation der weiteren Bibliotheken...")
    for package in packages:
        install_package(package)

    print_status("\nInstallation abgeschlossen. Bitte überprüfen Sie die oben genannten Meldungen auf Fehler oder Warnungen.")
    print_status("Sie können die Installation überprüfen, indem Sie Python starten und versuchen, die Bibliotheken zu importieren, z.B.: 'import pandas'.")

if __name__ == "__main__":
    # Überprüfen, ob das Skript mit Administratorrechten ausgeführt wird
    if platform.system() == "Windows":
        try:
            # Versuche, eine Datei in einem geschützten Verzeichnis zu schreiben
            # Dies ist ein einfacher Test für Administratorrechte
            test_file_path = os.path.join(os.environ.get("ProgramFiles", "C:\\Program Files"), "test_admin_write.tmp")
            with open(test_file_path, "w") as f:
                f.write("test")
            os.remove(test_file_path)
        except PermissionError:
            print_status("Dieses Skript muss mit Administratorrechten ausgeführt werden.", "ERROR")
            print_status("Bitte verwenden Sie die bereitgestellte BAT-Datei oder klicken Sie mit der rechten Maustaste auf die Skriptdatei und wählen Sie 'Als Administrator ausführen'.", "ERROR")
            sys.exit(1)
        except Exception as e:
            # Anderer Fehler, der nicht direkt mit Berechtigungen zusammenhängt, aber das Schreiben verhindert
            print_status(f"Konnte Administratorrechte nicht überprüfen: {e}", "WARNING")
            print_status("Stellen Sie sicher, dass Sie das Skript als Administrator ausführen.", "WARNING")
    main()
