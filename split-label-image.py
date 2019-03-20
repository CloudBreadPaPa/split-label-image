import os, random
from shutil import copyfile

#Each folder 60 images
#Each member 10 images

# setup folders
l = ["label_dir_01", "label_dir_02", "label_dir_03", "label_dir_04"]

# create member dir
members = ["0", "1", "2", "3", "4", "5"]
for member in members:
	os.makedirs("_member_" + member)

merge_dir = "_merge_all"

for idx in l:
	src_dir = idx
	dst = src_dir + "_60"
	#make dir
	os.makedirs(dst)
	for i in range(0,100):
		f = random.choice(os.listdir(src_dir))
		src_path = os.path.join(src_dir, f)
		dst_path = os.path.join(dst, f)
		#merge_path = os.path.join(merge_dir, f)
		#print(src_path)
		copyfile(src_path, dst_path)
		
		#rename file name
		full_rename = dst + "/" + src_dir + "_" + str(i) + ".jpg"
		print(full_rename)
		
		#copy this file to merge folders
		copyfile(src_path, merge_dir + "/" + src_dir + "_" + str(i) + ".jpg")
		
		# copy to member folder
		if i >= 0 and i < 10:
			copyfile(src_path, "_member_0/" + src_dir + "_" + str(i) + ".jpg")
		if i >= 10 and i < 20:
			copyfile(src_path, "_member_1/" + src_dir + "_" + str(i) + ".jpg")
		if i >= 20 and i < 30:
			copyfile(src_path, "_member_2/" + src_dir + "_" + str(i) + ".jpg")
		if i >= 30 and i < 40:
			copyfile(src_path, "_member_3/" + src_dir + "_" + str(i) + ".jpg")
		if i >= 40 and i < 50:
			copyfile(src_path, "_member_4/" + src_dir + "_" + str(i) + ".jpg")
		if i >= 50 and i < 60:
			copyfile(src_path, "_member_5/" + src_dir + "_" + str(i) + ".jpg")

		os.rename(dst_path, full_rename)
		
		# if loop count = 60 then break
		file_cnt = len([name for name in os.listdir(dst) if os.path.isfile(os.path.join(dst, name))])
		if file_cnt == 60:
			break
print("done")
