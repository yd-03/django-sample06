import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from django.db import transaction

from manager.models import Manager, Person, Worker


class Command(BaseCommand):
    help = "Create dummy data for Person, Manager, and Worker models"

    def handle(self, *args, **kwargs):
        try:
            with transaction.atomic():
                # 1. Personのデータを100件作成
                for i in range(100):
                    try:
                        birthdate = datetime.date(
                            year=1980 + i % 20, month=1 + (i % 12), day=1 + (i % 28)
                        )
                        Person.objects.create(
                            name="person{}".format(i),
                            birthdate=birthdate,
                            sex=Person.MAN,
                            address_from=Person.TOKYO,
                            current_address=Person.TOKYO,
                            email="person{}@gmail.com".format(i),
                        )
                    except ValueError as e:
                        self.stdout.write(
                            self.style.ERROR(f"Invalid date for person{i}: {e}")
                        )
                self.stdout.write(
                    self.style.SUCCESS("Successfully created 100 Persons")
                )

                # 2. Managerのデータを10件作成 (PersonのID 1～10を使用)
                dep_list = [
                    Manager.DEP_ACCOUNTING,
                    Manager.DEP_SALES,
                    Manager.DEP_PRODUCTION,
                    Manager.DEP_DEVELOPMENT,
                    Manager.DEP_HR,
                    Manager.DEP_FIN,
                    Manager.DEP_AFFAIRS,
                    Manager.DEP_PLANNING,
                    Manager.DEP_BUSINESS,
                    Manager.DEP_DISTR,
                    Manager.DEP_IS,
                ]

                for i in range(1, 11):  # PersonのIDが1～10の範囲でManagerを作成
                    try:
                        p = Person.objects.get(id=i)
                        join_at = datetime.date(
                            year=2005 + i % 10, month=1 + (i % 12), day=1 + (i % 28)
                        )
                        Manager.objects.create(
                            person=p, department=dep_list[i % 10], join_at=join_at
                        )
                    except ObjectDoesNotExist as e:
                        self.stdout.write(
                            self.style.ERROR(f"Person with id {i} does not exist: {e}")
                        )
                self.stdout.write(
                    self.style.SUCCESS("Successfully created 10 Managers")
                )

                # 3. Workerのデータを90件作成 (PersonのID 11～100を使用)
                for i in range(11, 101):  # PersonのIDが11～100の範囲でWorkerを作成
                    try:
                        p = Person.objects.get(id=i)
                        m = Manager.objects.get(
                            id=1 + (i % 10)
                        )  # ManagerのID 1～10を繰り返し使用
                        join_at = datetime.date(
                            year=2005 + i % 10, month=1 + (i % 12), day=1 + (i % 28)
                        )
                        Worker.objects.create(person=p, manager=m, join_at=join_at)
                    except ObjectDoesNotExist as e:
                        self.stdout.write(
                            self.style.ERROR(f"Person or Manager does not exist: {e}")
                        )
                self.stdout.write(self.style.SUCCESS("Successfully created 90 Workers"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"An error occurred: {e}"))
