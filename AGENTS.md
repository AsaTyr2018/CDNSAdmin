CDNSAdmin is a administrative Webinterface for coreDNS
Designed with a Modern and Easy to use WebUI.

## 📋 **Funktionsübersicht für CDNSAdmin**

---

## 🔧 **Zonenverwaltung**

| Funktion                        | Beschreibung                                                      | WebUI-Komponente            |
| ------------------------------- | ----------------------------------------------------------------- | --------------------------- |
| ✅ Anzeige aller Zonen           | Welche Domains CoreDNS aktuell verwaltet (`Corefile`-Zonenblöcke) | Dashboard                   |
| ✅ Zonen hinzufügen/löschen      | Neue Zone deklarieren (mit Dateipfad)                             | Formular                    |
| ✅ Zonen aktivieren/deaktivieren | Toggle in `Corefile` oder per Plugin-Steuerung                    | Schalter                    |
| ✅ DNS-Zonendateien bearbeiten   | TXT-Editor für `.db`-Dateien (z. B. BIND-Format)                  | Editor mit Syntax-Highlight |
| ✅ Live-Neuladen von Zonen       | `reload` Plugin nutzt Dateiänderungstrigger                       | Button/Automatik            |
| ✅ Serial erhöhen automatisch    | Für SOA nach jeder Änderung                                       | Auto-Update                 |
| ✅ Zonen validieren              | DNS-Zonenprüfung vor dem Speichern                                | Checker/Feedbackfeld        |

---

## 📁 **Corefile-Verwaltung**

| Funktion                            | Beschreibung                           | WebUI-Komponente      |
| ----------------------------------- | -------------------------------------- | --------------------- |
| ✅ `Corefile` anzeigen/bearbeiten    | Hauptkonfiguration für CoreDNS         | Haupteditor           |
| ✅ Blöcke verschieben / neu anordnen | Reihenfolge von Plugins/Blöcken ändern | Drag & Drop           |
| ✅ Plugins ein-/ausschalten          | Häkchen-UI oder Plugin-Builder         | Plugin-Menü           |
| ✅ Kommentarunterstützung            | Zeilen auskommentieren / dokumentieren | Texteditor mit Syntax |
| ✅ CoreDNS neustarten                | Soft- oder Hard-Reload                 | Button oben rechts 😏 |

---

## 🔌 **Plugin-Management**

| Funktion                       | Beschreibung                                    | WebUI-Komponente         |
| ------------------------------ | ----------------------------------------------- | ------------------------ |
| 🔎 Plugin-Erkennung            | Welche Plugins sind geladen/aktiv?              | Liste/Statusanzeige      |
| 🧩 Plugin konfigurieren        | z. B. `forward`, `file`, `log`, `template` etc. | Formular je Plugin       |
| 📡 Healthchecks anzeigen       | `health` Plugin Status (HTTP /metrics /health)  | Live-Anzeige             |
| 📈 `prometheus` Monitoring     | Integration für Stats                           | Button / Link zu Grafana |
| ✨ `template` Records editieren | Dynamische DNS-Einträge per Template-Plugin     | UI mit Vorschau          |

---

## 📡 **Live DNS Tools (Client-Tools im UI)**

| Funktion            | Beschreibung                               | WebUI-Komponente       |
| ------------------- | ------------------------------------------ | ---------------------- |
| 🔍 DNS Lookup       | Dig/Ping via UI                            | Eingabefeld + Ergebnis |
| ⏱ TTL-Anzeige       | TTL für Records anzeigen                   | Tooltip/Tabellenfeld   |
| 🧪 Zonen testen     | Simulierter DNS-Request intern             | "Test"-Button          |
| 🌐 Trace/Debug View | Logausgabe mit Filter für einzelne Domains | Log-Konsole            |

---

## 🔐 **Zugriff & Admin**

| Funktion                        | Beschreibung                     | WebUI-Komponente  |
| ------------------------------- | -------------------------------- | ----------------- |
| ✅ Passwort-Login                | Adminzugang                      | Loginseite        |
| ✅ Zugriffsbeschränkung per Netz | IP-Whitelisting für GUI-Zugang   | Konfigurierbar    |
| ✅ Backup von Zonen/Corefile     | ZIP-Export oder Git-Commit       | Backup-Menü       |
| 🔄 Restore-Funktion             | Alte Zone/Corefile zurückspielen | Restore-Dropdown  |
| 🗂 Versionshistorie             | Git oder Zeitstempel-Changelog   | Historie/Timeline |

---

