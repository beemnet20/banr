from django.test import TestCase
from .models import NuclearReactorConstructionProject, Expenditure, Contractor
from datetime import datetime

TEST_BUDGET = 4000000000
TEST_EXPENSE = 50000
TEST_DATE = datetime.today().strftime("%Y-%m-%d")


class TestModels(TestCase):

    def setUp(self):
        self.contractor1 = Contractor.objects.create(company_name="Test contractor1")
        self.contractor2 = Contractor.objects.create(company_name="Test contractor2")
        self.project = NuclearReactorConstructionProject.objects.create(
            project_name="Test project",
            city="Test city",
            state="Test state",
            zipcode="12345",
            project_status="active",
            project_phase="design",
            budget=TEST_BUDGET,
            power_rating_gw=1,
            notes="test"
        )
        self.project.contractors.add(self.contractor1)
        self.expense1 = Expenditure.objects.create(expense_name="Test expense1",
                                                  amount=TEST_EXPENSE,
                                                  project=self.project,
                                                  contractor=self.contractor1,
                                                  date_incurred = TEST_DATE)
        self.expense2 = Expenditure.objects.create(expense_name="Test expense2",
                                                  amount=TEST_EXPENSE,
                                                  project=self.project,
                                                  contractor=self.contractor2,
                                                  date_incurred=TEST_DATE)


    def test_project_creation(self):
        self.assertEqual(self.project.project_name, "Test project")
        self.assertEqual(self.project.city, "Test city")
        self.assertEqual(self.project.state, "Test state")
        self.assertEqual(self.project.zipcode, "12345")
        self.assertEqual(self.project.project_status, "active")
        self.assertEqual(self.project.project_phase, "design")
        self.assertEqual(self.project.budget, TEST_BUDGET)
        self.assertEqual(self.project.power_rating_gw, 1)
        self.assertEqual(self.project.total_expenses, TEST_EXPENSE*2)

    def test__contractors(self):
        self.assertEqual(self.project.contractors.count(), 1)
        self.assertIn(self.contractor1, self.project.contractors.all())
        self.assertNotIn(self.contractor2, self.project.contractors.all())

    def test_expenditures(self):
        self.expense2.delete()
        self.assertFalse(Expenditure.objects.filter(id=self.expense2.id).exists())
        self.assertEqual(self.project.total_expenses, TEST_EXPENSE)
