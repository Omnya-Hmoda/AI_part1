#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    results_dic = ()
    
    # Retrieve the filenames from the image directory
    in_files = listdir(image_dir) 
    word = in_files.lower().split('_')

    for idx in range(0, len(in_files), 1):
      if word.isalpha():
                pet_label += word + " "
    pet_label = pet_label.strip()
        
        # Add pet label to results dictionary
    if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
    else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    # Return the results dictionary
    return results_dic

# Test the function
if __name__ == "__main__":
    # Test the function with example directory
    image_dir = "pet_images/"
    results = get_pet_labels(image_dir)
    
    # Print first 10 key-value pairs for verification
    print("\nPrinting first 10 key-value pairs in dictionary results_dic:")
    count = 0
    for key, value in results.items():
        print("Filename=", key, "   Pet Label=", value[0])
        count += 1
        if count == 10:
            break