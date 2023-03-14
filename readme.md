# What is this script?
I've been a photographer for over a decade and have had to move digital versions of my photos to hard drives so many times that I've inevitably ended up with duplicates of files in folders with slightly different names. The script was made really simple to go through my ~600GB Photo Archive folder and only looks for exact copies of the file by name and size. I don't often rename my photos but editing will change the size, use the same name, and that's not a duplicate to me. If you're also a photographer and have a different workflow that you'd be interested in having me try to tailor this to include, let me know.
# How do I run it?
First, make sure you have Python 3 and can use it in your command line. You'll need the path to the parent directory where all your photos are stored, or you could always just drop the script into that directory and try running it there. With no arguments, it will run in the directory it's located in and the directory you want to run is relative to where the script is.

In the same directory:
`python3 file_checker.py`

In a different directory:
`python3 file_checker.py [dir_name]`

If you want to skip certain directories:
`python3 file_checker.py <dir_name> [dir_to_skip_name...]`

*The last option was created because I did intentionally copy some files into a folder called 'Cafes' and wanted to put off what to do with that until later. In my case it was python3 file_checker.py . Cafes*
## Is it worth it?
To me? Yes, totally. Depending on how organized you are with your photos, mileage may vary and it may vary with what camera you're using (mine are Sony a7 and FujiXF10 for digital). If you scan film, it's more than likely you have as many duplicates of the same scans as I did. Feel free to try it out and let me know what you think, it doesn't destroy anything (unless you have a file named 'duplicates.txt' in the script directory, in which case, wow, amazing coincidence) and at worst may give you information that's erroneous. Please make sure if you delete any photos you've also confirmed with your own eyes or computer's tools they are indeed the same.
## Can you add more file extensions?
Absolutely, I may even add some and forget to update this. But I did leave out a lot of raws since I usually use dng (I know, very shameful) but it's very easy to write in and I'd be glad to do it if there's any interest.
