import os
import sys
import zipfile
import tarfile
import shutil

def main():
	#parse params to get working director
	if len(sys.argv)==2:
		while 1:
			run = raw_input("\nThis script may be dangerous. Please be 10000% sure the target directory is the correct one that contains the zip file. Continue? (y/n): ")
			if run=='n':
				exit()
			elif run=='y':
				break
			else:
				print("you got two options")
	else:
		print("please specify directory")
		exit()
	os.chdir(sys.argv[1])
	#unzip and store original zip file
	oz = os.listdir(".")[0]
	#move all sub files to new dir, and set working directory there
	os.mkdir("Extracted")
	shutil.move(oz, "./Extracted")
	os.chdir("./Extracted")
	home = os.getcwd()
	Unzip(oz, False)
	print(os.listdir("."))
	shutil.move(oz, "..")
	#repeatedly call unzip command until no zip files exists
	running = True
	while running:
		for wd, _, files in os.walk('.'):
			running = UnzipAll(wd, files, home)
	#when done, ask user what to do with orig
#	while 1:
#		decision = raw_input("\nDelete original zip file? (y/n): ")
#		if decision=='y':
#			os.remove(oz)
#			break
#		elif decision=='n':
#			break
#		else:
#			print("you got two options")


def UnzipAll(wd, files, home):
	found = False
	exist, zips = ZipsExist(files)
	if not exist:
		found = False
	else:
		found = True
		os.chdir(wd)
		for f in zips:
			Unzip(f, True)
		os.chdir(home)
	return found


def ZipsExist(files):
	exist = False
	zips = list()
	for f in files:
		if f[-3:]==".gz" or f[-4:]==".tgz" or f[-4:]==".zip":
			exist = True
			zips.append(f)
	return exist,zips

#Unzip file and add its name to remove queue
def Unzip(zip_file, remove):
	if zip_file[-4:]==".tgz" or zip_file[-3:]==".gz":
		tar = tarfile.open(zip_file, "r:gz")
		tar.extractall()
		tar.close()
	elif zip_file[-4:]==".zip":
		zipf = zipfile.ZipFile(zip_file, mode='r')
		zipf.extractall()
		zipf.close()
	else:
		print("what's this file even??\n")
		exit()
	if remove and (zip_file[-4:]==".tgz" or zip_file[-4:]==".zip"):
		os.remove(zip_file)


if __name__ == '__main__':
	main()

