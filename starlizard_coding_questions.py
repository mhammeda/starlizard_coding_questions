# Question 1
def getMaximumOutfits(outfits, money):
	start_index = 0
	next_index = 1
	lookup = {}
	maximum_outfits = 0
	outfits_subset = None
	while (next_index <= len(outfits)):
		outfits_subset = outfits[start_index:next_index]
		if (sum(outfits_subset) <= money):
			if (len(outfits_subset) > maximum_outfits):
				maximum_outfits = len(outfits_subset)
			next_index = next_index + 1
		else:
			start_index = start_index + 1

	return maximum_outfits


# Question 2
def numDuplicates(name, price, weight):
	lookup = {}
	num_duplicates = 0
	n = len(name)

	for i in range(n):
		key_to_consider = name[i] + ","
		key_to_consider = key_to_consider + str(price[i])
		key_to_consider = key_to_consider + ","
		key_to_consider = key_to_consider + str(weight[i])
		if (key_to_consider in lookup):
			num_duplicates = num_duplicates + 1
		else:
			lookup[key_to_consider] = True

	return num_duplicates
