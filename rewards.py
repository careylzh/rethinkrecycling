import csv
import os

def write_to_csv(calculated_reward_amount, phone_number, file_name='rewards.csv'):
    """
    Writes calculated reward amount and phone number to a CSV file.

    Parameters:
    - calculated_reward_amount (float): The reward amount to write.
    - phone_number (str): The phone number associated with the reward.
    - file_name (str): The name of the CSV file (default is 'rewards.csv').

    Returns:
    - None
    """
    # Check if the file exists
    file_exists = os.path.isfile(file_name)

    # Open the file in append mode
    with open(file_name, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header if the file does not exist
        if not file_exists:
            writer.writerow(['Calculated_Reward_Amount', 'Phone_Number'])

        # Write the data
        writer.writerow([calculated_reward_amount, phone_number])

        #testting
        