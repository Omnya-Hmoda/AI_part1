import os

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the filenames
    of the images contain the true identity of the pet in the image.
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be classified 
                 by the classifier function (string)
                 
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. The list contains the following item:
                      index 0 = pet image label (string)
    """
    # Check if image_dir is a valid directory
    if not os.path.isdir(image_dir):
        print(f"Error: {image_dir} is not a valid directory.")
        return None

    try:
        in_files = os.listdir(image_dir) 
    except Exception as e:
        print(f"Error reading directory {image_dir}: {e}")
        return None

    results_dic = dict()

    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":
            pet_label = ""
            low_pet_image = in_files[idx].lower()
            word_list_pet_image = low_pet_image.split("_")

            for word in word_list_pet_image:
                if word.isalpha():
                    pet_label += word + " "

            pet_label = pet_label.strip()

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print(f"Warning: Duplicate files exist in directory {in_files[idx]}")

    return results_dic

# Example usage
image_dir = 'intropyproject-classify-pet-images/pet_images'
results = get_pet_labels(image_dir)
if results is not None:
    print(results)
