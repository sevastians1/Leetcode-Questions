def bottle_song(num):
	if num==1:
		print("1 bottle of beer on the wall, 1 bottle of beer. \
			 Take one down and pass it around, no more bottles of beer on the wall. \
			 \nNo more bottles of beer on the wall, no more bottles of beer.\
			 Go to the store and buy some more, 99 bottles of beer on the wall.")
		return
	print(f'{num} bottles of beer on the wall, {num} bottles of beer. \
		 Take one down and pass it around, {num-1} bottles of beer on the wall.')
	bottle_song(num-1)
bottle_song(99)
