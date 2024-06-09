# Pandas Refresher

## Setting up your environment

Pandas is an external package, we have to install it

But before that, we want to create an isolated box containing packages just for your project

You don't want this box to interfere with your other projects

### Step 1: Create your environment box - This contains only packages you need for your project

We have already made it easy for your computer to create this box
- `pyproject.toml` and `poetry.lock`

Optional Detail:
- `pyproject.toml` defines the range of library versions you can use
- But `poetry.lock` makes it easy for you; it gives you a strict version to use

Create the box and enter it with

```commandline
poetry shell

clement@Clements-Laptop introduction_to_python % poetry shell
Spawning shell within /Users/clement/Library/Caches/pypoetry/virtualenvs/your-project-name-XfBLCSwF-py3.11
clement@Clements-Laptop introduction_to_python % emulate bash -c '. /Users/clement/Library/Caches/pypoetry/virtualenvs/your-project-name-XfBLCSwF-py3.11/bin/activate'

clement@Clements-Laptop introduction_to_python % 
```

Notice that you have a new () to the left of your commandline conline

`(your-project-name-py3.11)` <- you are now using this box

## Exercises

1. Reading CSV files into a pd.DataFrame
- pd.read_csv

```commandline
(your-project-name-py3.11) clement@Clements-Laptop lesson_6_revision_on_pandas % python 001_reading_a_csv_file.py 
         name              title  age           town
0       aaron           lovebird   32        yew tee
1     clement            wagebro   29  choa chu kang
2       elson   ahmad of malacca   29        hougang
3  zheng yang    targetted by xi   29          tibet
4      eugene   prince of taiwan   29  choa chu kang
5        gabe           casanova   29        yew tee
6    wei xuan  play grandma card   29  choa chu kang
```

2. Selecting rows by condition, or by indexes

This returns a copy of your pd.DataFrame / columns (pd.Series)

- pd.DataFrame.loc[mask, list_of_columns]
- pd.DataFrame.iloc[range_of_row_indexes, range_of_column_indexes]

Getting first 3 rows with iloc

```commandline
(your-project-name-py3.11) clement@Clements-Laptop lesson_6_revision_on_pandas % python 002_select_first_three_rows_with_iloc.py 
      name             title  age           town
0    aaron          lovebird   32        yew tee
1  clement           wagebro   29  choa chu kang
2    elson  ahmad of malacca   29        hougang
```

Get only Eugene and Gabe

```commandline
(your-project-name-py3.11) clement@Clements-Laptop lesson_6_revision_on_pandas % python 002_select_only_eugene_and_gabe.py 
     name             title  age           town
4  eugene  prince of taiwan   29  choa chu kang
5    gabe          casanova   29        yew tee
```

3. Ordering rows in Data Frame by column

This returns a copy of your pd.DataFrame, if inplace=False

- pd.DataFrame.sort_values(list_of_columns, ascending=True, inplace=False)

```commandline
(your-project-name-py3.11) clement@Clements-Laptop lesson_6_revision_on_pandas % python 003_sorting_data_frame.py 
sorted_df
         name              title  age           town
0       aaron           lovebird   32        yew tee
1     clement            wagebro   29  choa chu kang
2       elson   ahmad of malacca   29        hougang
4      eugene   prince of taiwan   29  choa chu kang
5        gabe           casanova   29        yew tee
6    wei xuan  play grandma card   29  choa chu kang
3  zheng yang    targetted by xi   29          tibet
df -> to show you the original df is not edited
         name              title  age           town
0       aaron           lovebird   32        yew tee
1     clement            wagebro   29  choa chu kang
2       elson   ahmad of malacca   29        hougang
3  zheng yang    targetted by xi   29          tibet
4      eugene   prince of taiwan   29  choa chu kang
5        gabe           casanova   29        yew tee
6    wei xuan  play grandma card   29  choa chu kang
```

4. Check the type of all columns in a pd.DataFrame

df.info()

```commandline
(your-project-name-py3.11) clement@Clements-Laptop lesson_6_revision_on_pandas % python 004_check_all_column_types.py
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 7 entries, 0 to 6
Data columns (total 4 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   name    7 non-null      object
 1   title   7 non-null      object
 2   age     7 non-null      int64 
 3   town    7 non-null      object
dtypes: int64(1), object(3)
memory usage: 356.0+ bytes
```

5. Check the type of a single column (pd.Series)

series.dtype

```commandline
(your-project-name-py3.11) clement@Clements-Laptop lesson_6_revision_on_pandas % python 005_check_type_of_a_single_column.py 
object
```

6. Casting a pd.Series (column) in a pd.DataFrame into another type

This returns a new pd.Series but with the type casted to int32

df["my_age"].astype("int32")

Then you can assign this copy back to the pd.DataFrame

df["my_age"] = df["my_age"].astype("int32")