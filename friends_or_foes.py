{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0906c39a",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'list' object has no attribute 'spilt'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[3], line 2\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[38;5;66;03m# profile = input().split()\u001b[39;00m\n\u001b[0;32m----> 2\u001b[0m profile \u001b[38;5;241m=\u001b[39m \u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mJohn\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mHHHHDH\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mspilt\u001b[49m()  \u001b[38;5;66;03m# Example input for testing\u001b[39;00m\n\u001b[1;32m      3\u001b[0m name \u001b[38;5;241m=\u001b[39m profile[\u001b[38;5;241m0\u001b[39m]\n\u001b[1;32m      4\u001b[0m honesty_arr \u001b[38;5;241m=\u001b[39m profile[\u001b[38;5;241m1\u001b[39m:]\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'list' object has no attribute 'spilt'"
     ]
    }
   ],
   "source": [
    "profile = input().split()\n",
    "print(profile)  # Example input for testing\n",
    "name = profile[0]\n",
    "honesty_arr = profile[1:]\n",
    "dishonesty_count = 0\n",
    "\n",
    "for x in honesty_arr:\n",
    "    if x == 'D':\n",
    "        dishonesty_count += 1\n",
    "        \n",
    "percentage = (dishonesty_count/len(profile))*100\n",
    "\n",
    "if percentage < 1.0:\n",
    "    print('H')\n",
    "else:\n",
    "    print('D')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
