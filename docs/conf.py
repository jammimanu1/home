import sys
import os

project = 'Trézor Documentation'
copyright = '2024, Trézor'
author = 'Trézor Team'

release = '1.0.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx_copybutton',
]

templates_path = ['_templates']
html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'furo'

html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#1c7b43",
        "color-brand-content": "#1c7b43",
    },
    "dark_css_variables": {
        "color-brand-primary": "#2ea563",
        "color-brand-content": "#2ea563",
    },
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "announcement": "Official Trézor Documentation",
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Important settings to prevent 404 errors
html_baseurl = 'https://trezor-docs.readthedocs.io'
html_permalinks = True
html_permalinks_icon = '¶'
html_copy_source = False
html_show_sourcelink = False

# SEO settings
html_title = "Trézor Suite (Official) | Desktop & Web Crypto® Management"
meta_description = "Trézor Suite is your secure, all-in-one interface to manage cryptocurrencies with Trézor Hardware Wallet. Learn how to set up, connect, and secure your assets via desktop and web.",
meta_keywords = "Trézor Suite, Trézor Wallet, Trézor Bridge, Trézor.io/start, Hardware Wallet, Trézor Login"
html_short_title = "Trézor Docs"
language = 'en'

# -- Add custom schema.org JSON-LD markup -----------------------------------

def setup(app):
    app.add_js_file(None, body="""
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "Trézor Suite",
      "url": "https://public-suite-trezr.readthedocs.io/en/latest/",
      "description": "Secure your crypto assets with Trézor Suite – your all-in-one platform for managing Trezor hardware wallets.",
      "publisher": {
        "@type": "Organization",
        "name": "Trézor suite"
      }
    }
    </script>
    """)
