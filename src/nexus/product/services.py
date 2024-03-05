from django.db import connection
from collections import namedtuple


def namedtuplefetchall(cursor):
    """Return all rows from a cursor  as a namedtuple"""
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def dictfetchall(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    """Return one row from a cursor as a dict"""
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))


def get_latest_products(count, *kwargs):
    with connection.cursor() as cursor:
        # where = ''
        # if kwargs.get('city')!= f'{city.id}' and kwargs.get('category') != f'category.id':
        #     where = f'where cc.id={kwargs["category"]} or cc.parent_id={kwargs.get('category')} and cc2.id={kwargs["city"]}'
        # elif kwargs.get('city')!='':
        #     where = f'cc2.id={kwargs.get('city')}'
        # elif kwargs.get('category') != '':
        #     where = f'where cc.id={kwargs.get('category')} or cc.parent_id={kwargs.get('category')}'

        cursor.execute("""
                select pp.*, cc.name as category_name, gc.name as city_name, uu.first_name || ' ' || uu.last_name as fullname, 
                pp2.image as product_image 
                from product_product pp
                inner join category_category cc on cc.id = pp.category_id
                inner join geo_city gc on gc.id = pp.city_id
                inner join user_user uu on uu.id = pp.user_id
                inner join product_productimage pp2 on pp.id = pp2.product_id and pp2.is_main is True
                
                order by pp.post_date desc
                limit 6
        """)
        return dictfetchall(cursor)
