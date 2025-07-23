```markdown
# 🐍 Python-Installationsskript für Finanz- und Data-Science-Bibliotheken

Dieses Repository enthält ein Python-Skript sowie eine Batch-Datei, mit denen Sie gängige Finanz- und Data-Science-Bibliotheken unter Windows automatisiert installieren können. Damit wird die Einrichtung einer passenden Entwicklungsumgebung erheblich vereinfacht.

---

## 📚 Inhalt

- [Beschreibung](#beschreibung)
- [Wichtiger Hinweis](#wichtiger-hinweis)
- [Unterstützte Bibliotheken](#unterstützte-bibliotheken)
- [Voraussetzungen](#voraussetzungen)
- [Installation & Nutzung](#installation--nutzung)
- [Fehlerbehebung](#fehlerbehebung)
- [Lizenz](#lizenz)
- [Autoren](#autoren)

---

## 📝 Beschreibung

Das Skript richtet sich an Einsteiger und Fortgeschrittene, die häufig mit Python im Bereich **Finanzanalyse**, **Data Science** und **Machine Learning** arbeiten. Die Installation erfolgt automatisiert und spart so Zeit und Aufwand.

---

## ⚠️ Wichtiger Hinweis

> **Dieses Skript ist ausschließlich für die Verwendung auf einem _Windows 11 64-Bit PC_ konzipiert.**  
> Es nutzt Windows-spezifische Befehle und Annahmen (z.B. für die TA-Lib-Installation und die Administratorrechte).

---

## 📦 Unterstützte Bibliotheken

Folgende Bibliotheken werden aktuell installiert:

- **TA-Lib:** Technische Analyse-Bibliothek (besondere Installationsschritte, siehe unten)
- **Flask:** Web-Framework für die Entwicklung von Webanwendungen
- **Matplotlib:** Umfassende Bibliothek für statische, animierte und interaktive Visualisierungen in Python
- **NumPy:** Grundlegendes Paket für wissenschaftliches Rechnen mit Python, insbesondere für Arrays und mathematische Funktionen
- **Pandas:** Datenanalyse- und -manipulationsbibliothek, die DataFrames bereitstellt
- **scikit-learn:** Bibliothek für Machine Learning (Klassifikation, Regression, Clustering usw.)
- **SciPy:** Bibliothek für wissenschaftliches und technisches Rechnen
- **Seaborn:** Datenvisualisierungsbibliothek basierend auf Matplotlib, die eine High-Level-Schnittstelle für attraktive statistische Grafiken bietet
- **Jupyter:** Für interaktives Computing (Jupyter Notebook/Lab)
- **yfinance:** Zum Herunterladen von Finanzmarktdaten von Yahoo! Finance
- **Statsmodels:** Zum Schätzen verschiedener statistischer Modelle und für statistische Tests
- **OpenPyXL:** Zum Lesen und Schreiben von Excel 2010 xlsx/xlsm/xltx/xltm-Dateien
- **mplfinance:** Eine Matplotlib-Finanz-Plotting-Bibliothek für Finanzdaten (z.B. Candlestick-Charts)
- **requests:** Elegante und einfache HTTP-Anfragen für Python (nützlich für API-Interaktionen)
- **BeautifulSoup4:** Für das Parsen von HTML- und XML-Dokumenten (nützlich für Web Scraping)

---

## 🖥️ Voraussetzungen

- **Windows 11 64-Bit Betriebssystem**
- **Installiertes Python (Version 3.8 oder höher, 64-Bit):** Das Skript prüft die Python-Version.
- **Administratorrechte:** Die Ausführung des Skripts erfordert Administratorrechte, da Bibliotheken global installiert werden. Die bereitgestellte Batch-Datei handhabt dies automatisch.
- **Internetverbindung:** Eine aktive Internetverbindung ist erforderlich, um die Bibliotheken herunterzuladen.

---

## 🚀 Installation & Nutzung

### 1. Repository herunterladen

- Als ZIP herunterladen und entpacken **oder**
- Mit Git klonen:
  ```bash
  git clone https://github.com/KOGTI-2023/Python-Installationsskript-fuer-Finanz-und-Data-Science-Bibliotheken.git
  ```

### 2. Dateien vorbereiten

- Stellen Sie sicher, dass sich die Dateien `install_finance_libs.py` **und** `start_install.bat` im selben Ordner befinden.

### 3. Installation starten (**empfohlen**)

- Doppelklicken Sie auf die Datei **start_install.bat**.
- Die Batch-Datei startet das Python-Skript automatisch mit Administratorrechten. Bestätigen Sie ggf. die Benutzerkontensteuerung (UAC), falls sie erscheint.

### 4. Alternativ: Python-Skript direkt ausführen (mit Administratorrechten)

- Öffnen Sie eine **Eingabeaufforderung (CMD) als Administrator** im Verzeichnis des Skripts und führen Sie aus:
  ```bash
  python install_finance_libs.py
  ```

### 5. Jupyter Notebook starten (optional)

- Nach der erfolgreichen Installation können Sie ein Jupyter Notebook starten, um Ihre Entwicklungsumgebung zu testen:
  ```bash
  jupyter notebook
  ```

---

## 🛠️ Fehlerbehebung

- **Administratorrechte:**  
  Stellen Sie sicher, dass das Skript mit Administratorrechten ausgeführt wird. Die `start_install.bat` sollte dies automatisch handhaben.

- **Python im PATH:**  
  Vergewissern Sie sich, dass Python und pip korrekt installiert und in der **PATH-Variable** Ihres Systems hinterlegt sind.

- **TA-Lib Installation:**  
  Die Installation von TA-Lib kann auf Windows herausfordernd sein. Das Skript versucht, die passende `.whl`-Datei automatisch herunterzuladen. Sollte dies fehlschlagen, überprüfen Sie die Fehlermeldungen im Konsolenfenster.

- **Visual C++ Build Tools:**  
  Bei einigen Bibliotheken, die kompiliert werden müssen (insbesondere wenn die TA-Lib `.whl`-Installation fehlschlägt und eine direkte `pip install TA-Lib` versucht wird), benötigen Sie eventuell die "Build Tools für Visual Studio".

- **Internetverbindung:**  
  Stellen Sie sicher, dass Sie eine stabile Internetverbindung haben.

- **Konsolenausgabe:**  
  Lesen Sie die Ausgaben im Konsolenfenster sorgfältig durch. Fehlermeldungen geben oft Aufschluss über das Problem.

---

## 📄 Lizenz

MIT License

---

## 👤 Autoren

KOGTI-2023 @ 07/2025

