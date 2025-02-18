# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../lib/'))


# -- Project information -----------------------------------------------------

project = u'odgi'
copyright = '2020-2022, Guarracino A., Heumos S., Nahnsen S., Prins P., Garrison E. Revision v0.7.1-07f261c'
author = u'Andrea Guarracino, Simon Heumos, Sven Nahnsen , Pjotr Prins, Erik Garrison'

# The short X.Y version
version = 'v0.7.1'
# The full version, including alpha/beta/rc tags
release = '07f261c'


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'm2r2', 'sphinx.ext.autosectionlabel']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = ["_themes", ]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'odgidoc'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'odgi.tex', u'odgi documentation',
     u'Andrea Guarracino, Simon Heumos, Sven Nahnsen , Pjotr Prins, Erik Garrison', 'manual'),
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# we list the authors seperately
EG = 'Erik Garrison'
AG = 'Andrea Guarracino'
SH = 'Simon Heumos'
man_pages = [
    ('man/odgi', 'odgi', u'Dynamic succinct variation graph tool.',
     [author], 1),
    ('man/odgi_bin', 'odgi_bin', u'Binning of pangenome sequence and path information in the graph.',
     [EG, SH], 1),
    ('man/odgi_break', 'odgi_break', u'Break cycles in the graph and drop its paths.',
     [EG], 1),
    ('man/odgi_build', 'odgi_build', u'Construct a dynamic succinct variation graph in ODGI format from a GFAv1.',
     [EG], 1),
    ('man/odgi_chop', 'odgi_chop', u'Divide nodes into smaller pieces preserving node topology and order.',
     [EG, AG], 1),
    ('man/odgi_cover', 'odgi_cover', u'Cover the graph with paths.',
     [AG], 1),
    ('man/odgi_pav', 'odgi_pav', u'Presence/absence variants (PAVs).',
     [AG], 1),
    ('man/odgi_degree', 'odgi_degree', u'Describe the graph in terms of node degree.',
     [EG], 1),
    ('man/odgi_heaps', 'odgi_heaps', u'Path pangenome coverage permutations.',
     [EG], 1),
    ('man/odgi_depth', 'odgi_depth', u'Find the depth of a graph as defined by query criteria. Without specifying any '
                                     u'non-mandatory options, it prints in a tab-delimited format path, start, end, '
                                     u'and mean.depth to stdout.',
     [AG], 1),
    ('man/odgi_draw', 'odgi_draw', u'Draw previously-determined 2D layouts of the graph with diverse annotations.',
     [EG], 1),
    ('man/odgi_explode', 'odgi_explode', u'Breaks a graph into connected components storing each component in its own '
                                         u'file.',
     [AG], 1),
    ('man/odgi_extract', 'odgi_extract', u'Extract subgraphs or parts of a graph defined by query criteria.',
     [AG], 1),
    ('man/odgi_flatten', 'odgi_flatten', u'Generate linearizations of a graph.',
     [EG], 1),
    ('man/odgi_groom', 'odgi_groom', u'Resolve spurious inverting links.',
     [EG, AG], 1),
    ('man/odgi_kmers', 'odgi_kmers', u'Display and characterize the kmer space of a graph.',
     [EG], 1),
    ('man/odgi_layout', 'odgi_layout', u'Establish 2D layouts of the graph using path-guided stochastic gradient '
                                       u'descent (the graph must be sorted and id-compacted).',
     [EG, AG, SH], 1),
    ('man/odgi_matrix', 'odgi_matrix', u'Write the graph topology in sparse matrix formats.',
     [EG], 1),
    ('man/odgi_normalize', 'odgi_normalize', u'Compact unitigs and simplify redundant furcations.',
     [EG], 1),
    ('man/odgi_overlap', 'odgi_overlap', u'Find the paths touched by given input paths.',
     [AG], 1),
    ('man/odgi_panpos', 'odgi_panpos', u'Get the pangenome position of a given path and nucleotide position (1-based).',
     [SH], 1),
    ('man/odgi_pathindex', 'odgi_pathindex', u'Create a path index for a given graph.',
     [SH], 1),
    ('man/odgi_paths', 'odgi_paths', u'Interrogate the embedded paths of a graph. Does not print anything to stdout '
                                     u'by default!',
     [EG], 1),
    ('man/odgi_position', 'odgi_position', u'Find, translate, and liftover graph and path positions between graphs. '
                                           u'Results are printed to stdout.',
     [EG], 1),
    ('man/odgi_prune', 'odgi_prune', u'Remove parts of the graph.',
     [EG], 1),
    ('man/odgi_server', 'odgi_server', u'Start a basic HTTP server with a given path index file to go from '
                                       u'*path:position* to *pangenome:position* very efficiently.',
     [SH], 1),
    ('man/odgi_sort', 'odgi_sort', u'Apply different kinds of sorting algorithms to a graph. The most prominent one '
                                   u'is the PG-SGD sorting algorithm.',
     [SH, AG, EG], 1),
    ('man/odgi_squeeze', 'odgi_squeeze', u'Squeezes multiple graphs in ODGI format into the same file in ODGI format.',
     [AG], 1),
    ('man/odgi_stats', 'odgi_stats', u'Metrics describing a variation graph and its path relationship.',
     [EG, AG], 1),
    ('man/odgi_test', 'odgi_test', u'Run ODGI unit tests.',
     [EG, SH, AG], 1),
    ('man/odgi_unchop', 'odgi_unchop', u'Merge unitigs into a single node preserving the node order.',
     [EG, AG], 1),
    ('man/odgi_unitig', 'odgi_unitig', u'Output unitigs of the graph.',
     [EG], 1),
    ('man/odgi_validate', 'odgi_validate', u'Validate a graph checking if the paths are consistent with the graph '
                                           u'topology.',
     [AG], 1),
    ('man/odgi_version', 'odgi_version', u'Print the version of ODGI to stdout.',
     [SH], 1),
    ('man/odgi_view', 'odgi_view', u'Project a graph into other formats.',
     [EG], 1),
    ('man/odgi_viz', 'odgi_viz', u'Visualize a variation graph in 1D.',
     [EG, AG], 1),
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'odgi', u'odgi Documentation',
     author, 'odgi', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# we don't want smart quotes
smartquotes = False
