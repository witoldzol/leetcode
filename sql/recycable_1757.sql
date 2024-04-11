-- https://leetcode.com/problems/recyclable-and-low-fat-products/
select product_id from Products
where low_fats='Y' and recyclable='Y'

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    return df['product_id'].to_frame()

