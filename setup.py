from setuptools import setup, find_packages

setup(
    name="wifi-password-auditor",
    version="1.0.0",
    description="A Wi-Fi password security auditing tool for educational use",
    author="Your Name",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "PyYAML>=6.0.1",
        "reportlab>=4.0.9",
        "tqdm>=4.66.1",
    ],
    python_requires=">=3.9",
    entry_points={
        "console_scripts": [
            "wifi-auditor=wifi_auditor.main:main",
        ],
    },
)
