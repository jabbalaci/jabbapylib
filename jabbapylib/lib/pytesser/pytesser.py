#!/usr/bin/env python

"""
OCR in Python using the Tesseract engine from Google
http://code.google.com/p/pytesser/
by Michael J.T. O'Kelly
V 0.0.1, 3/10/07

some slight customizations by Jabba
"""

import os    # Jabba
import Image
import sys
import util
import errors

from subprocess import Popen, STDOUT
import jabbapylib.config as cfg

DEBUG = False

tesseract_exe_name = cfg.MY_TESSERACT # Name of executable to be called at command line
scratch_image_name = "/tmp/tesseract_tmp.bmp" # This file must be .bmp or other Tesseract-compatible format
scratch_text_name_root = "/tmp/tesseract_txt" # Leave out the .txt extension
cleanup_scratch_flag = True  # Temporary files cleaned up after OCR operation


def call_tesseract(input_filename, output_filename):
	"""Calls external tesseract.exe on input file (restrictions on types),
	outputting output_filename+'txt'"""
	dest = open(os.devnull, 'w')    # Jabba
	if DEBUG:
		dest = STDOUT
	args = [tesseract_exe_name, input_filename, output_filename]
	proc = Popen(args, stdout=dest, stderr=dest)    # Jabba
	retcode = proc.wait()
	if retcode != 0:
		errors.check_for_errors()

def image_to_string(im, cleanup = cleanup_scratch_flag):
	"""Converts im to file, applies tesseract, and fetches resulting text.
	If cleanup=True, delete scratch files after operation."""
	try:
		util.image_to_scratch(im, scratch_image_name)
		call_tesseract(scratch_image_name, scratch_text_name_root)
		text = util.retrieve_text(scratch_text_name_root)
	finally:
		if cleanup:
			util.perform_cleanup(scratch_image_name, scratch_text_name_root)
	return text

def image_file_to_string(filename, cleanup = cleanup_scratch_flag, graceful_errors=True):
	"""Applies tesseract to filename; or, if image is incompatible and graceful_errors=True,
	converts to compatible format and then applies tesseract.  Fetches resulting text.
	If cleanup=True, delete scratch files after operation."""
	try:
		try:
			call_tesseract(filename, scratch_text_name_root)
			text = util.retrieve_text(scratch_text_name_root)
		#except errors.Tesser_General_Exception:
		except:
			if graceful_errors:
				im = Image.open(filename)
				text = image_to_string(im, cleanup)
			else:
				raise
	finally:
		if cleanup:
			util.perform_cleanup(scratch_image_name, scratch_text_name_root)
	return text
	

if __name__=='__main__':
#	im = Image.open('tests/phototest.tif')
#	text = image_to_string(im)
#	print text
#	try:
#		text = image_file_to_string('tests/fnord.tif', graceful_errors=False)
#	except errors.Tesser_General_Exception, value:
#		print "tests/fnord.tif is incompatible filetype.  Try graceful_errors=True"
#		print value
#	text = image_file_to_string('tests/fnord.tif', graceful_errors=True)
#	print "tests/fnord.tif contents:", text
#	text = image_file_to_string('tests/fonts_test.png', graceful_errors=True)
#	print text
	if len(sys.argv) == 1:
		print "Usage: {0} <image_file>".format(sys.argv[0])
		sys.exit(1)
	# else
	img = Image.open(sys.argv[1])
	text = image_to_string(img)
	print text
