# imports

from numba import njit
import numpy as np

# -------------------------------------------------

# initialise numba compiler
@njit

def find_peaks_numpy(x,prominence=None):
    # define the size of the dataset and cancel code when smaller than 3
    n= x.size
    if n < 3:
        return np.empty(0,dtype=np.int64)

    # pre-define dynamic numba lists for peaks and prominences
    peaks= []
    prominences= []

    # start iterating through all data
    i = 1
    while i < n-1:
        # check wether you have found a peak/plateau
        if x[i] > x[i-1]:
            plat_start= i
            plat_end= i

            # find wether you are on a flat plateau and where it ends
            while plat_end < n-1 and x[plat_end] == x[plat_end - 1]:
                plat_end += 1

            # when you have found the entire plateau, find the middle
            if plat_end < n-1 and x[plat_end] > x[plat_end + 1]:
                peak_idx= (plat_start + plat_end) // 2
                peak_val= x[peak_idx]

                # start prominence calculation
                # scan left valley
                left_val= peak_val
                for j in range(plat_start -1,-1,-1):
                    if x[j] > peak_val:
                        break
                    if x[j] < left_val:
                        left_val= x[j]

                # scan right valley
                right_val= peak_val
                for j in range(plat_end + 1,n):
                    if x[j] > peak_val:
                        break
                    if x[j] < right_val:
                        right_val= x[j]

                # find the depth of the valley/the prominence
                lowest_contour= max(left_val,right_val)
                prom= peak_val - lowest_contour

                # filter out the peaks with too little prominence
                if prom >= prominence:
                    peaks.append(peak_idx)
                    prominences.append(prom)

            # index the upper loop to the rest of the data
            i= plat_end + 1
        else:
            i += 1
            
    return np.array(peaks,dtype=np.int64)