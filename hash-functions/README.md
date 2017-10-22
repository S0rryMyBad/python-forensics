A **hash function** is defined as the function that maps on a large amount of data to a fixed value with a specified length. This function ensures that the same input results in the same output, which is actually defined as a hash sum. Hash sum includes a characteristic with specified information. This function is practically impossible to revert. Thus, any third party attack like brute force attack is practically impossible. Also, this kind of algorithm is called **one-way cryptographic algorithm**.

An ideal cryptographic hash function has four main properties:
* it must be easy to compute the hash value for any given input.
* it must be infeasible to generate the original input from it's hash.
* it must be infeasible to modify the input without changing the hash.
* it must be infeasible to find two different inputs with the same hash.
