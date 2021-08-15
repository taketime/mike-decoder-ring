from stego_lsb.LSBSteg import recover_data

recover_data(
    steg_image_path="happy_birthday_mike.png",
    output_file_path="birthday_song.mp3",
    num_lsb=7,
)

print(
    "HELLO MIKE\n\nHappy 40th!\n\nis there something new in this directory?\n\nmaybe a fun track\n\n-- pete and chris\n"
)
