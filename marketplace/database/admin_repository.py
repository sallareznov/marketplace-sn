from attr import frozen
from dataset import Database

from marketplace.domain.admin import Admin


# https://dataset.readthedocs.io/
@frozen
class AdminRepository:
    database: Database

    # TODO handle password
    # TODO move "create table" query to SQL migration file
    def create_table(self):
        self.database["admin"].query(
            """
                CREATE TABLE IF NOT EXISTS admin(
                    id TEXT PRIMARY KEY,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    phone_number TEXT NOT NULL
                )
            """
        )

        self.database.commit()

    def create_admin(self, admin: Admin):
        pass
