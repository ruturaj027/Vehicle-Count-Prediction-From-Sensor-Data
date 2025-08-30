{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ee715a55-dcbf-40f4-bf78-11a05b55ee5e",
   "metadata": {},
   "source": [
    "#Vehicle Count Prediction From Sensor Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9462534b-7354-40d3-95be-2542efe73157",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>DateTime</th>\n",
       "      <th>Vehicles</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2015-11-01 00:00:00</td>\n",
       "      <td>15</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2015-11-01 01:00:00</td>\n",
       "      <td>13</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2015-11-01 02:00:00</td>\n",
       "      <td>10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2015-11-01 03:00:00</td>\n",
       "      <td>7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2015-11-01 04:00:00</td>\n",
       "      <td>9</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "              DateTime  Vehicles\n",
       "0  2015-11-01 00:00:00        15\n",
       "1  2015-11-01 01:00:00        13\n",
       "2  2015-11-01 02:00:00        10\n",
       "3  2015-11-01 03:00:00         7\n",
       "4  2015-11-01 04:00:00         9"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# importing the pandas module for data frame\n",
    "import pandas as pd\n",
    "\n",
    "# load the data set into train variable.\n",
    "train = pd.read_csv(\"C:/Users/rutur/Downloads/vehicles.csv\")\n",
    "\n",
    "# display top 5 values of dataset\n",
    "train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "21572811-8add-4d03-8b75-e19861b0f1ea",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>DateTime</th>\n",
       "      <th>Vehicles</th>\n",
       "      <th>date</th>\n",
       "      <th>weekday</th>\n",
       "      <th>hour</th>\n",
       "      <th>month</th>\n",
       "      <th>year</th>\n",
       "      <th>dayofyear</th>\n",
       "      <th>weekofyear</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2015-11-01 00:00:00</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>11</td>\n",
       "      <td>2015</td>\n",
       "      <td>305</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2015-11-01 01:00:00</td>\n",
       "      <td>13</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>11</td>\n",
       "      <td>2015</td>\n",
       "      <td>305</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2015-11-01 02:00:00</td>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>2</td>\n",
       "      <td>11</td>\n",
       "      <td>2015</td>\n",
       "      <td>305</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2015-11-01 03:00:00</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>3</td>\n",
       "      <td>11</td>\n",
       "      <td>2015</td>\n",
       "      <td>305</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2015-11-01 04:00:00</td>\n",
       "      <td>9</td>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>4</td>\n",
       "      <td>11</td>\n",
       "      <td>2015</td>\n",
       "      <td>305</td>\n",
       "      <td>44</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             DateTime  Vehicles  date  weekday  hour  month  year  dayofyear  \\\n",
       "0 2015-11-01 00:00:00        15     1        6     0     11  2015        305   \n",
       "1 2015-11-01 01:00:00        13     1        6     1     11  2015        305   \n",
       "2 2015-11-01 02:00:00        10     1        6     2     11  2015        305   \n",
       "3 2015-11-01 03:00:00         7     1        6     3     11  2015        305   \n",
       "4 2015-11-01 04:00:00         9     1        6     4     11  2015        305   \n",
       "\n",
       "   weekofyear  \n",
       "0          44  \n",
       "1          44  \n",
       "2          44  \n",
       "3          44  \n",
       "4          44  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# function to get all data from timestamp, getdate\n",
    "def get_dom(dt):\n",
    "\treturn dt.day\n",
    "# get week day\n",
    "def get_weekday(dt):\n",
    "\treturn dt.weekday()\n",
    "# get hour\n",
    "def get_hour(dt):\n",
    "\treturn dt.hour\n",
    "# get year\n",
    "def get_year(dt):\n",
    "\treturn dt.year\n",
    "# get month\n",
    "def get_month(dt):\n",
    "\treturn dt.month\n",
    "# get year day\n",
    "def get_dayofyear(dt):\n",
    "\treturn dt.dayofyear\n",
    "# get year week\n",
    "def get_weekofyear(dt):\n",
    "\treturn dt.weekofyear\n",
    "\n",
    "train['DateTime'] = train['DateTime'].map(pd.to_datetime)\n",
    "train['date'] = train['DateTime'].map(get_dom)\n",
    "train['weekday'] = train['DateTime'].map(get_weekday)\n",
    "train['hour'] = train['DateTime'].map(get_hour)\n",
    "train['month'] = train['DateTime'].map(get_month)\n",
    "train['year'] = train['DateTime'].map(get_year)\n",
    "train['dayofyear'] = train['DateTime'].map(get_dayofyear)\n",
    "train['weekofyear'] = train['DateTime'].map(get_weekofyear)\n",
    "\n",
    "# display\n",
    "train.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "286c5795-db38-4469-bffe-42c248ba6233",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   date  weekday  hour  month  year  dayofyear  weekofyear\n",
      "0     1        6     0     11  2015        305          44\n",
      "1     1        6     1     11  2015        305          44\n",
      "2     1        6     2     11  2015        305          44\n",
      "3     1        6     3     11  2015        305          44\n",
      "4     1        6     4     11  2015        305          44\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "0    15\n",
       "1    13\n",
       "2    10\n",
       "3     7\n",
       "4     9\n",
       "Name: Vehicles, dtype: int64"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# there is no use of DateTime module so remove it\n",
    "train = train.drop(['DateTime'], axis=1)\n",
    "\n",
    "# separating class label for training the data\n",
    "train1 = train.drop(['Vehicles'], axis=1)\n",
    "\n",
    "# class label is stored in target\n",
    "target = train['Vehicles']\n",
    "\n",
    "print(train1.head())\n",
    "target.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b2f17efe-a681-4609-997c-1906bc19cbfc",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\rutur\\AppData\\Roaming\\Python\\Python312\\site-packages\\sklearn\\utils\\validation.py:2749: UserWarning: X does not have valid feature names, but RandomForestRegressor was fitted with feature names\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "array([9.31885714])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#importing Random forest\n",
    "from sklearn.ensemble import RandomForestRegressor\n",
    "\n",
    "#defining the RandomForestRegressor\n",
    "m1=RandomForestRegressor()\n",
    "\n",
    "m1.fit(train1,target)\n",
    "#testing\n",
    "m1.predict([[11,6,0,1,2015,11,2]])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c511af01-a6da-45d5-a284-3800ade6c8cb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
