from __future__ import absolute_import, unicode_literals
from .models import SKU
import csv,sys
from celery import shared_task
import io


@shared_task
def handle_uploaded_file(uploaded_file_path):
    print('handling file')
    count = 0
    with open(uploaded_file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                #print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                try:
                    _, create = SKU.objects.update_or_create(
                        sku     = row[1],
                        defaults={
                            'name' : row[0],
                            'description' : row[2]
                            }
                    )
                except:
                    print("Error:{}\n{}".format(row,sys.exc_info()))
                #print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
    print(f'Processed {line_count} lines.')
    return f'Processed {line_count} lines.'