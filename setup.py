from setuptools import setup, find_packages

setup(
    name="my_manim_lib",
    version="0.2.1",
    description="Custom Manim animations, mobjects, and creatures",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "my_manim_lib": [
            "STATUS.md",
            "assets/*.svg",
        ]
    },
    install_requires=[
        "manim",
        "numpy",
        "scipy",
        "matplotlib",
    ],
    python_requires=">=3.9",
)
