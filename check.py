import chromadb

c = chromadb.PersistentClient(path='D:/MyKB/chroma_db')
col = c.get_or_create_collection(name='my_kb', embedding_function=None)
data = col.get(include=['documents', 'metadatas'])

if data['ids']:
    print('\n===== 数据库最后一条记录的内容 =====')
    print(data['documents'][-1][:1000])
    print('\n===== 元数据 =====')
    print(data['metadatas'][-1])
else:
    print('\n数据库是空的，还没有索引任何文件。')