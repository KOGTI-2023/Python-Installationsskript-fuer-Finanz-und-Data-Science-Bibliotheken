# 🚀 Automatisierte Python-Umgebung für Finanzanalyse & Data Science

Dieses Repository enthält ein **Python-Skript**, das die Einrichtung einer Entwicklungsumgebung für Finanzanalysen und Data Science automatisiert. Es installiert alle notwendigen Bibliotheken, einschließlich der oft problematischen **TA-Lib**, mit nur wenigen Klicks.

---

## 🏆 Hauptmerkmale

- **Interaktive Installation:** Das Skript fragt Sie, ob die Bibliotheken global oder in einer virtuellen Umgebung (`.venv`) installiert werden sollen. Die Verwendung einer virtuellen Umgebung wird dringend empfohlen, um Projekt-Abhängigkeiten zu isolieren.
- **Automatisierte Bibliotheksinstallation:** Installiert über 15 essentielle Bibliotheken für Datenanalyse, maschinelles Lernen und Finanztools.
- **Spezialisierte TA-Lib-Installation:** Behebt häufige Installationsprobleme von TA-Lib unter Windows, indem die passende Wheel-Datei automatisch heruntergeladen und installiert wird.
- **Einfache Handhabung:** Ein einzelnes Skript erledigt den gesamten Installationsprozess für Sie.

---

## ⚙️ Voraussetzungen

> **Bitte vor Ausführung sicherstellen:**
>
> - **Betriebssystem:** Windows 11 (64-Bit)
> - **Python:** Python 3.8 oder neuer (64-Bit), installiert und im `PATH` verfügbar
> - **Berechtigungen:** Administratorrechte für bestimmte Aktionen
> - **Internet:** Aktive Internetverbindung zum Herunterladen der Bibliotheken

---

## 📋 Anleitung

Folgen Sie diesen Schritten, um Ihre Umgebung einzurichten:

### 1. Repository herunterladen

- Klonen Sie dieses Repository **oder** laden Sie es als ZIP-Datei herunter.

### 2. Installation starten

- Öffnen Sie eine Kommandozeile (`cmd` oder PowerShell), navigieren Sie in das Verzeichnis mit dem Skript und führen Sie folgenden Befehl aus:

```powershell
python install_finance_libs.py
```

### 3. Installationsmethode wählen

- Das Skript startet und begrüßt Sie mit einem Menü:

```text
Wählen Sie eine Installationsmethode:
[1] Global (Alle Benutzer)
[2] In einer virtuellen Umgebung (.venv)
[3] Beenden
```

- **Option 1 (Global):** Die Bibliotheken werden direkt in Ihrem Haupt-Python-Installationspfad installiert.
- **Option 2 (Virtuelle Umgebung):** Das Skript erstellt einen neuen Ordner `.venv` im selben Verzeichnis und installiert alle Bibliotheken dort. **Empfohlen!**

### 4. Aktivierung der virtuellen Umgebung (nur bei Option 2)

- Nach der Installation in einer virtuellen Umgebung aktivieren Sie diese mit:

  **Windows:**

  ```powershell
  .\.venv\Scripts\activate
  ```

- Nach der Aktivierung können Sie die installierten Bibliotheken in Ihrem Projekt verwenden.

---

## 🛠️ Fehlerbehebung

- **"Python nicht gefunden":** Stellen Sie sicher, dass Python installiert und zur `PATH`-Umgebungsvariable hinzugefügt wurde.
- **TA-Lib-Fehler:** Das Skript versucht, dies zu beheben. Sollte es dennoch fehlschlagen, laden Sie die passende TA-Lib Wheel-Datei manuell von der [Gohlke-Website](https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib) herunter und legen Sie sie in den Skript-Ordner, bevor Sie das Skript erneut ausführen
