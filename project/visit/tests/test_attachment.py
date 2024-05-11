from django.test import TestCase
from visit.models import Attachment
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from unittest.mock import patch, MagicMock

class AttachmentAPITestCase(TestCase):

    def setUp(self):
        self.attachment_data = {'file': SimpleUploadedFile("test.txt", b"file_content"), 'notes': "Test notes"}

    @patch('visit.views.AttachmentViewSet')
    def test_attachment_api_list(self, MockAttachment):
        mock_attachment = MagicMock()
        mock_attachment.file.name = 'attachments/test.txt'
        MockAttachment.objects.all.return_value = [mock_attachment]

        response = self.client.get(reverse('attachment-list'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, 'attachments/test.txt')

    @patch('visit.views.AttachmentViewSet')
    def test_attachment_api_detail(self, MockAttachment):
        mock_attachment = MagicMock()
        mock_attachment.file.name = 'attachments/test.txt'
        mock_attachment.notes = 'Test notes'
        MockAttachment.objects.get.return_value = mock_attachment

       
        # response = self.client.get(reverse('attachment-detail', kwargs={'pk': 1}))
        # self.assertEqual(response.status_code, 200)
        # # self.assertContains(response, 'attachments/test.txt')
        # self.assertContains(response, 'Test notes')

    # @patch('visit.views.AttachmentViewSet')
    # def test_attachment_api_create(self, MockAttachment):
    #     MockAttachment.objects.create.return_value = MagicMock()

    #     response = self.client.post(reverse('attachment-list'), self.attachment_data, format='multipart')
    #     self.assertEqual(response.status_code, 201)
    #     self.assertTrue(MockAttachment.objects.create.called)

    # @patch('myapp.views.AttachmentViewSet')
    # def test_attachment_api_update(self, MockAttachment):
    #     mock_attachment_instance = MagicMock()
    #     MockAttachment.objects.get.return_value = mock_attachment_instance

    #     response = self.client.put(reverse('attachment-detail', kwargs={'pk': 1}), self.attachment_data, format='multipart')
    #     self.assertEqual(response.status_code, 200)
    #     mock_attachment_instance.save.assert_called_once()

    # @patch('myapp.views.AttachmentViewSet')
    # def test_attachment_api_delete(self, MockAttachment):
    #     mock_attachment_instance = MagicMock()
    #     MockAttachment.objects.get.return_value = mock_attachment_instance

    #     response = self.client.delete(reverse('attachment-detail', kwargs={'pk': 1}))
    #     self.assertEqual(response.status_code, 204)
    #     mock_attachment_instance.delete.assert_called_once()
