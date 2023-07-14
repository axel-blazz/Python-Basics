country_data = open('countries.txt', 'a')

country_data.write('\nThis is a new line.')

#if we use w we can create new files even and it overwrites existing files.
# Without \n here this text wouldnt be in the next line.

country_data.close()