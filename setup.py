from setuptools import setup, find_packages

try:
    with open("requirements.txt", "r", encoding="utf-8") as f:
        install_requires = [l.strip() for l in f if l.strip() and not l.startswith("#")]
except FileNotFoundError:
    install_requires = []

setup(
    name="ai_inventory_fc",
    version="0.0.1",
    description="AI Inventory FC (Frappe app)",
    author="Your Name / Org",
    author_email="you@example.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
