from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ai_inventory_fc",
    version="0.1.0",
    description="Lightweight AI inventory & sales forecast app compatible with ERPNext and deployable on Frappe Cloud.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="you@example.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
