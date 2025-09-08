# AI-Powered Penetration Testing Tool

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)

A comprehensive, AI-powered penetration testing tool designed for medium-scale web applications and network infrastructures. This tool combines traditional security scanning techniques with machine learning to provide intelligent vulnerability analysis and simplified reporting suitable for technical and non-technical stakeholders.

## 🔥 Features

### Core Capabilities
- **Network Scanning**: Advanced port scanning, service detection, and network reconnaissance
- **Web Application Testing**: Comprehensive vulnerability scanning including:
  - SQL Injection detection
  - Cross-Site Scripting (XSS) testing
  - Command Injection identification
  - File Inclusion vulnerability discovery
  - Security header analysis
  - SSL/TLS configuration assessment
- **AI-Powered Analysis**: Machine learning-based vulnerability prioritization and risk assessment
- **Intelligent Reporting**: Automated generation of executive summaries with simplified explanations

### AI/ML Integration
- **Vulnerability Severity Prediction**: ML models trained to assess vulnerability severity
- **Risk Scoring**: Intelligent risk calculation based on multiple factors
- **Attack Vector Identification**: Automated identification of potential attack paths
- **Natural Language Explanations**: AI-generated explanations suitable for non-technical audiences
- **Remediation Suggestions**: Context-aware remediation recommendations

### User Interface Options
- **Command Line Interface**: Powerful CLI for automated scanning and integration
- **Graphical User Interface**: User-friendly GUI for interactive scanning
- **Report Generation**: HTML and JSON report formats with visualizations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Network access to targets
- Administrative privileges (for some scanning features)

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/Jason1806/FYP.git
cd FYP
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Install the package** (optional):
```bash
pip install -e .
```

### Basic Usage

#### Command Line Interface

**Network and Web Application Scan**:
```bash
python -m pentestool.main scan -t example.com --ai-analysis
```

**Web Application Only**:
```bash
python -m pentestool.main webapp -t https://example.com
```

**Custom Port Range**:
```bash
python -m pentestool.main scan -t 192.168.1.1 -p 1-65535 --output report.html
```

#### Graphical User Interface

Launch the GUI application:
```bash
python -m pentestool.main gui
```

## 📊 Report Examples

### Executive Summary
The tool generates executive summaries that explain security findings in simple terms:

```
EXECUTIVE SECURITY ASSESSMENT SUMMARY

Overall Risk Level: High (Score: 75/100)

Key Findings:
• Total vulnerabilities identified: 12
• Critical severity issues: 2
• High severity issues: 4

Immediate Actions Required:
• Address 2 critical vulnerabilities immediately
• Prioritize resolution of 4 high-severity issues
```

### Simplified Explanations
Each vulnerability type includes explanations designed for non-technical stakeholders:

> **What is SQL Injection?**
> Imagine your website's database is like a filing cabinet, and SQL injection is like someone tricking 
> the filing system into giving them access to files they shouldn't see...

## 🔧 Configuration

The tool uses a configuration file located at `~/.pentestool/config.json`. Key settings include:

```json
{
  "scan_settings": {
    "default_ports": "1-1000",
    "timeout": 10,
    "enable_ai_analysis": true
  },
  "report_settings": {
    "output_format": "html",
    "include_charts": true,
    "simplified_explanations": true
  }
}
```

## 🏗️ Building Executable

To create a standalone executable:

1. **Install PyInstaller**:
```bash
pip install pyinstaller
```

2. **Build the executable**:
```bash
pyinstaller pentestool.spec
```

The executable will be created in the `dist/` directory.

## 📁 Project Structure

```
FYP/
├── pentestool/
│   ├── core/           # Core scanning modules
│   │   ├── scanner.py  # Network scanning
│   │   └── webapp.py   # Web application scanning
│   ├── ai/             # AI/ML components
│   │   └── analyzer.py # Vulnerability analysis
│   ├── reports/        # Report generation
│   │   └── generator.py
│   ├── gui/            # GUI components
│   │   └── main_window.py
│   ├── utils/          # Utility modules
│   │   └── config.py
│   └── main.py         # Main entry point
├── requirements.txt    # Python dependencies
├── setup.py           # Package setup
├── pentestool.spec    # PyInstaller configuration
└── README.md          # This file
```

## 🧠 AI/ML Features

### Vulnerability Severity Prediction
The tool uses machine learning models to predict vulnerability severity based on:
- Vulnerability type and characteristics
- Affected services and ports
- Potential impact factors
- Historical vulnerability data

### Risk Assessment Algorithm
Risk scoring considers:
- Number and severity of vulnerabilities
- Attack surface size
- Service exposure
- Potential business impact

### Natural Language Generation
AI-powered explanations convert technical findings into:
- Executive summaries
- Simple vulnerability explanations
- Actionable remediation guidance
- Business impact assessments

## 🎯 Scanning Capabilities

### Network Scanning
- Port scanning with service detection
- Operating system fingerprinting
- SSL/TLS certificate analysis
- DNS enumeration and subdomain discovery
- Network service vulnerability assessment

### Web Application Testing
- **Input Validation**: SQL injection, XSS, command injection
- **Authentication**: Login bypass, session management
- **Authorization**: Access control testing
- **Information Disclosure**: Sensitive file detection
- **Configuration**: Security headers, SSL settings
- **File Inclusion**: Local and remote file inclusion

### AI-Enhanced Analysis
- Automated vulnerability prioritization
- Intelligent false positive reduction
- Context-aware remediation suggestions
- Business impact assessment
- Attack vector mapping

## 📈 Report Generation

### HTML Reports
- Executive dashboard with risk metrics
- Detailed vulnerability listings
- Visual charts and graphs
- Simplified explanations section
- Technical details for developers

### JSON Reports
- Machine-readable format
- API integration friendly
- Detailed metadata
- Structured vulnerability data

## ⚠️ Legal and Ethical Use

**IMPORTANT**: This tool is designed for legitimate security testing purposes only.

### Authorized Use Only
- Only scan systems you own or have explicit permission to test
- Obtain proper authorization before conducting security assessments
- Follow responsible disclosure practices for discovered vulnerabilities

### Educational Purpose
This tool is developed as part of a Final Year Project (FYP) for educational purposes and to demonstrate AI integration in cybersecurity tools.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Dependencies

Key libraries used:
- **python-nmap**: Network scanning
- **requests**: HTTP communications
- **beautifulsoup4**: HTML parsing
- **scikit-learn**: Machine learning
- **tensorflow**: Deep learning (optional)
- **nltk**: Natural language processing
- **matplotlib**: Chart generation
- **jinja2**: Report templating
- **rich**: Enhanced CLI output
- **tkinter**: GUI framework

## 📞 Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Check the documentation
- Review existing issues and discussions

## 🏆 Acknowledgments

- Developed as part of Final Year Project (FYP)
- Inspired by industry-standard penetration testing methodologies
- Utilizes open-source security tools and libraries
- AI/ML integration for enhanced vulnerability analysis

---

**Disclaimer**: This tool is for educational and authorized security testing purposes only. Users are responsible for compliance with applicable laws and regulations.