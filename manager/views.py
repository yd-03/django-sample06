from django.shortcuts import render
from django.views.generic import TemplateView

from manager.models import *


class WorkerListView(TemplateView):
    template_name = "worker_list.html"

    # HTTP GET リクエストを処理するメソッドを定義
    def get(self, request, *args, **kwargs):
        # 親クラスの get_context_data メソッドを呼び出して基本的なコンテキストデータを取得
        context = super(WorkerListView, self).get_context_data(**kwargs)
        # Worker モデルのすべてのインスタンスを取得
        workers = Worker.objects.all()
        # 取得した workers をコンテキストに追加
        context["workers"] = workers
        # テンプレートをレンダリングし、HTTP レスポンスを返す
        return render(request, self.template_name, context)
