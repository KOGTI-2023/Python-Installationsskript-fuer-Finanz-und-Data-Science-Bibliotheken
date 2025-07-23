# [**Python-Installationsskript für Finanz- und Data-Science-Bibliotheken**](https://gemini.google.com/app/9203ee6fbc457c10)

---

Dieses Repository enthält ein Python-Skript sowie eine Batch-Datei, mit denen Sie gängige Finanz- und Data-Science-Bibliotheken unter Windows automatisiert installieren können. Damit wird die Einrichtung einer passenden Entwicklungsumgebung erleichtert.

[**Sehen Sie sich die interaktive Infografik an\!**](Infografik.html)

## **Inhalt**

* [Beschreibung](https://www.google.com/search?q=%23beschreibung)  
* [Wichtiger Hinweis](https://www.google.com/search?q=%23wichtiger-hinweis)  
* [Unterstützte Bibliotheken](https://www.google.com/search?q=%23unterst%C3%BCtzte-bibliotheken)  
* [Voraussetzungen](https://www.google.com/search?q=%23voraussetzungen)  
* [Installation & Nutzung](https://www.google.com/search?q=%23installation--nutzung)  
* [Fehlerbehebung](https://www.google.com/search?q=%23fehlerbehebung)  
* [Lizenz](https://www.google.com/search?q=%23lizenz)  
* [Autoren](https://www.google.com/search?q=%23autoren)

## **Beschreibung**

Das Skript richtet sich an Einsteiger und Fortgeschrittene, die häufig mit Python im Bereich Finanzanalyse, Data Science und Machine Learning arbeiten. Die Installation erfolgt automatisiert und ist speziell für Windows-Nutzer konzipiert.

## **Wichtiger Hinweis**

**Dieses Skript ist ausschließlich für die Verwendung auf einem Windows 11 64-Bit PC konzipiert.** Es nutzt Windows-spezifische Befehle und Annahmen (z.B. für die TA-Lib-Installation und die Administratorrechte-Handhabung der Batch-Datei). Die Ausführung auf anderen Betriebssystemen (Linux, macOS) wird nicht unterstützt und kann zu Fehlern führen.

## **Unterstützte Bibliotheken**

Folgende Bibliotheken werden aktuell installiert:

* **TA-Lib**: Technische Analyse-Bibliothek (besondere Installationsschritte, siehe unten)  
* **Flask**: Web-Framework für die Entwicklung von Webanwendungen  
* **Matplotlib**: Umfassende Bibliothek für statische, animierte und interaktive Visualisierungen in Python  
* **NumPy**: Grundlegendes Paket für wissenschaftliches Rechnen mit Python, insbesondere für Arrays und mathematische Funktionen  
* **Pandas**: Datenanalyse- und \-manipulationsbibliothek, die DataFrames bereitstellt  
* **scikit-learn**: Bibliothek für Machine Learning (Klassifikation, Regression, Clustering usw.)  
* **SciPy**: Bibliothek für wissenschaftliches und technisches Rechnen  
* **Seaborn**: Datenvisualisierungsbibliothek basierend auf Matplotlib, die eine High-Level-Schnittstelle für attraktive statistische Grafiken bietet  
* **Jupyter**: Für interaktives Computing (Jupyter Notebook/Lab)  
* **yfinance**: Zum Herunterladen von Finanzmarktdaten von Yahoo\! Finance  
* **Statsmodels**: Zum Schätzen verschiedener statistischer Modelle und für statistische Tests  
* **OpenPyXL**: Zum Lesen und Schreiben von Excel 2010 xlsx/xlsm/xltx/xltm-Dateien  
* **mplfinance**: Eine Matplotlib-Finanz-Plotting-Bibliothek für Finanzdaten (z.B. Candlestick-Charts)  
* **requests**: Elegante und einfache HTTP-Anfragen für Python (nützlich für API-Interaktionen)  
* **BeautifulSoup4**: Für das Parsen von HTML- und XML-Dokumenten (nützlich für Web Scraping)

## **Voraussetzungen**

* **Windows 11 64-Bit Betriebssystem**  
* **Installiertes Python (Version 3.8 oder höher, 64-Bit)**: Das Skript prüft die Python-Version.  
* **Administratorrechte**: Die Ausführung des Skripts erfordert Administratorrechte, da Bibliotheken global installiert werden. Die bereitgestellte Batch-Datei handhabt dies automatisch.  
* **Internetverbindung**: Eine aktive Internetverbindung ist erforderlich, um die Bibliotheken herunterzuladen.

## **Installation & Nutzung**

1. **Repository herunterladen**  
   Entweder als ZIP herunterladen und entpacken oder mit git klonen:  
   git clone https://github.com/KOGTI-2023/Python-Installationsskript-fuer-Finanz-und-Data-Science-Bibliotheken.git

2. **Dateien vorbereiten**  
   Stellen Sie sicher, dass sich die Dateien install\_finance\_libs.py und start\_install.bat im selben Ordner befinden.  
3. **Installation starten (empfohlen)**  
   Doppelklicken Sie auf die Datei start\_install.bat.  
   Die Batch-Datei startet das Python-Skript automatisch mit Administratorrechten. Bestätigen Sie die Benutzerkontensteuerung (UAC), falls sie erscheint.  
4. **Alternativ: Python-Skript direkt ausführen (mit Administratorrechten)**  
   Öffnen Sie eine Eingabeaufforderung (CMD) **als Administrator** im Verzeichnis des Skripts und führen Sie aus:  
   python install\_finance\_libs.py

5. **Jupyter Notebook starten (optional)**  
   Nach der erfolgreichen Installation können Sie ein Jupyter Notebook starten, um Ihre Entwicklungsumgebung zu testen:  
   jupyter notebook

## **Fehlerbehebung**

* **Administratorrechte**: Stellen Sie sicher, dass das Skript mit Administratorrechten ausgeführt wird. Die start\_install.bat sollte dies automatisch handhaben.  
* **Python im PATH**: Vergewissern Sie sich, dass Python und pip korrekt installiert und in der PATH-Variable Ihres Systems hinterlegt sind.  
* **TA-Lib Installation**: Die Installation von TA-Lib kann auf Windows herausfordernd sein. Das Skript versucht, die passende .whl-Datei automatisch herunterzuladen. Sollte dies fehlschlagen, überprüfen Sie die Fehlermeldungen in der Konsole. Möglicherweise müssen Sie die .whl-Datei manuell von einer Quelle wie [Unofficial Windows Binaries for Python Extension Packages](https://www.google.com/search?q=https://www.lfd.uci.edu/~gohlke/pythonlibs/%23ta-lib) herunterladen und im selben Ordner wie das Skript ablegen. Das Skript wird dann versuchen, diese lokale Datei zu verwenden.  
* **Visual C++ Build Tools**: Bei einigen Bibliotheken, die kompiliert werden müssen (insbesondere wenn die TA-Lib .whl-Installation fehlschlägt und eine direkte pip install TA-Lib versucht wird), benötigen Sie möglicherweise die "Build Tools für Visual Studio". Diese können von der Microsoft-Website heruntergeladen werden.  
* **Internetverbindung**: Stellen Sie sicher, dass Sie eine stabile Internetverbindung haben.  
* **Konsolenausgabe**: Lesen Sie die Ausgaben im Konsolenfenster sorgfältig durch. Fehlermeldungen geben oft Aufschluss über das Problem.

## **Lizenz**

[MIT License](https://www.google.com/search?q=LICENSE)

## **Autoren**

* [KOGTI-2023](https://github.com/KOGTI-2023)

# **Python Installation Script for Finance and Data Science Libraries**

This repository contains a Python script and a Batch file to automate the installation of common finance and data science libraries on Windows. This facilitates setting up a suitable development environment.

[**View the interactive Infographic\!**](https://www.google.com/search?q=Infografik.html)

## **Table of Contents**

* [Description](https://www.google.com/search?q=%23description)  
* [Important Note](https://www.google.com/search?q=%23important-note)  
* [Supported Libraries](https://www.google.com/search?q=%23supported-libraries)  
* [Prerequisites](https://www.google.com/search?q=%23prerequisites)  
* [Installation & Usage](https://www.google.com/search?q=%23installation--usage)  
* [Troubleshooting](https://www.google.com/search?q=%23troubleshooting)  
* [License](https://www.google.com/search?q=%23license)  
* [Authors](https://www.google.com/search?q=%23authors)

## **Description**

This script is aimed at beginners and advanced users who frequently work with Python in the fields of financial analysis, data science, and machine learning. The installation is automated and specifically designed for Windows users.

## **Important Note**

**This script is designed exclusively for use on a Windows 11 64-bit PC.** It utilizes Windows-specific commands and assumptions (e.g., for TA-Lib installation and the Batch file's administrator rights handling). Execution on other operating systems (Linux, macOS) is not supported and may lead to errors.

## **Supported Libraries**

The following libraries are currently installed:

* **TA-Lib**: Technical Analysis Library (special installation steps, see below)  
* **Flask**: Web framework for developing web applications  
* **Matplotlib**: Comprehensive library for creating static, animated, and interactive visualizations in Python  
* **NumPy**: Fundamental package for scientific computing with Python, especially for arrays and mathematical functions  
* **Pandas**: Data analysis and manipulation library, providing DataFrames  
* **scikit-learn**: Machine learning library (classification, regression, clustering, etc.)  
* **SciPy**: Library for scientific and technical computing  
* **Seaborn**: Data visualization library based on Matplotlib, providing a high-level interface for attractive statistical graphics  
* **Jupyter**: For interactive computing (Jupyter Notebook/Lab)  
* **yfinance**: For downloading financial market data from Yahoo\! Finance  
* **Statsmodels**: For estimating various statistical models and performing statistical tests  
* **OpenPyXL**: For reading and writing Excel 2010 xlsx/xlsm/xltx/xltm files  
* **mplfinance**: A Matplotlib finance plotting library for financial data (e.g., candlestick charts)  
* **requests**: Elegant and simple HTTP requests for Python (useful for API interactions)  
* **BeautifulSoup4**: For parsing HTML and XML documents (useful for web scraping)

## **Prerequisites**

* **Windows 11 64-bit Operating System**  
* **Installed Python (Version 3.8 or higher, 64-bit)**: The script checks the Python version.  
* **Administrator Privileges**: Running the script requires administrator privileges as libraries are installed globally. The provided Batch file handles this automatically.  
* **Internet Connection**: An active internet connection is required to download the libraries.

## **Installation & Usage**

1. **Download Repository**  
   Either download as a ZIP and extract, or clone with git:  
   git clone https://github.com/KOGTI-2023/Python-Installationsskript-fuer-Finanz-und-Data-Science-Bibliotheken.git

2. **Prepare Files**  
   Ensure that install\_finance\_libs.py and start\_install.bat are in the same folder.  
3. **Start Installation (recommended)**  
   Double-click the start\_install.bat file.  
   The Batch file will automatically launch the Python script with administrator privileges. Confirm the User Account Control (UAC) prompt if it appears.  
4. **Alternativ: Run Python Script Directly (with Administrator Privileges)**  
   Open a Command Prompt (CMD) **as Administrator** in the script's directory and execute:  
   python install\_finance\_libs.py

5. **Start Jupyter Notebook (optional)**  
   After successful installation, you can start a Jupyter Notebook to test your development environment:  
   jupyter notebook

## **Troubleshooting**

* **Administrator Privileges**: Ensure the script is run with administrator privileges. The start\_install.bat should handle this automatically.  
* **Python in PATH**: Verify that Python and pip are correctly installed and added to your system's PATH environment variable.  
* **TA-Lib Installation**: TA-Lib installation can be challenging on Windows. The script attempts to automatically download the appropriate .whl file. If this fails, check the error messages in the console. You might need to manually download the .whl file from a source like [Unofficial Windows Binaries for Python Extension Packages](https://www.google.com/search?q=https://www.lfd.uci.edu/~gohlke/pythonlibs/%23ta-lib) and place it in the same folder as the script. The script will then attempt to use this local file.  
* **Visual C++ Build Tools**: For some libraries that require compilation (especially if the TA-Lib .whl installation fails and a direct pip install TA-Lib is attempted), you might need the "Build Tools for Visual Studio". These can be downloaded from the Microsoft website.  
* **Internet Connection**: Ensure you have a stable internet connection.  
* **Console Output**: Carefully read the output in the console window. Error messages often provide clues about the problem.

## **License**

[MIT License](https://www.google.com/search?q=LICENSE)

## **Authors**

* [KOGTI-2023](https://github.com/KOGTI-2023)