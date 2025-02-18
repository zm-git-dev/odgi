.. _odgi flip:

#########
odgi flip
#########

Flip (reverse complement) paths to match the graph.

SYNOPSIS
========

**odgi flip** [**-i, --input**\ =\ *FILE*] [*OPTION*]…

DESCRIPTION
===========

The odgi flip command converts BED records against graph paths into new paths labeled by the BED record name.
Flip allows us to import genome annotations as paths, and is useful to produce input to odgi untangle.

OPTIONS
=======

MANDATORY OPTIONS
--------------

| **-i, --input**\ =\ *FILE*
| Load the succinct variation graph in ODGI format from this *FILE*. The file name usually ends with *.og*. It also accepts GFAv1, but the on-the-fly conversion to the ODGI format requires additional time!

| **-o, --out**\ =\ *FILE*
| Write the graph with fliped paths to *.og*.

Threading
---------

| **-t, --threads**\ =\ *N*
| Number of threads to use for parallel operations.

Processing Information
----------------------

| **-P, --progress**
| Print information about the operations and the progress to stderr.

Program Information
-------------------

| **-h, --help**
| Print a help message for **odgi flip**.

..
	EXIT STATUS
	===========

	| **0**
	| Success.

	| **1**
	| Failure (syntax or usage error; parameter error; file processing
	  failure; unexpected error).

	BUGS
	====

	Refer to the **odgi** issue tracker at
	https://github.com/pangenome/odgi/issues.
