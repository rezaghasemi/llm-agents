from setuptools import setup, find_packages

setup(
    name="llm-agents",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # add any runtime dependencies if needed
)
