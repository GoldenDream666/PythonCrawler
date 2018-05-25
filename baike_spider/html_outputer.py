# coding=utf-8

# HTML 输出器
class HtmlOutputer(object):

    # 初始化数据集为空
    def __init__(self):

        self.datas = []

    # 收集数据用来最后输出
    def collect_data(self, data):

        if data is None:
            return

        self.datas.append(data)

    # 按照 html 格式输出
    def output_html(self):
        """

        :rtype: object
        """
        fout = open('output.html', 'w')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")

        # Python 默认是 ASCII 码，设置为 UTF-8
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td> %s </td>" % data['url'].encode('utf-8'))
            fout.write("<td> %s </td>" % data['title'].encode('utf-8'))
            fout.write("<td> %s </td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()