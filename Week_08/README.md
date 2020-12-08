# 学习笔记
## 位运算及其实战要点
1. 位运算符<br>
   按位或 |<br>
   按位与 &<br>
   按位取反 ~<br>
   按位异或（相同为0，不同为1） ^<br>
2. XOR-异或<br>
   x^0 = x<br>
   x^1s = ~x (1s为全1，~0)<br>
   x^(~x) = 1s<br>
   x^x = 0<br>
   c = a^b => b = a^c => a = b^c //交换两个数<br>
   a^b^c = a^(b^c) = (a^b)^c<br>
3. **指定位置的位运算**
   将x最右边n位清零：x&(~0 << n)<br>
   获取x的第n位值（0或1）：(x>>n)&1<br>
   获取x的第n位的幂值：x&(1 << n)<br>
   仅将第n位置1：x|(1 << n)<br>
   仅将第n位置0：x&(~(1 << n))<br>
   将x最高位到第n位(含)清零：x&((1 << n)-1)<br>
4. **实战要点**
   + 判断奇偶
      x%2 == 1 => (x&1) == 1
      x%2 == 0 => (x&1) == 0
    + x>>1 => x/2<br>
       即:x=x/2 => x = x>>1 ; mid = (left+right)/2 => mid = (left+right)>>1
    + x = x&(x-1) 清零最低位的1
    + x&-x 得到最低位的1
    + x&~x=0

> ps: 计算机里都是以补码的形式计算 <br>

## 布隆过滤器
1. 一个很长的二进制向量和一系列随机映射函数。可用于检验一个元素是否在一个集合中（元素所有索引位只要有一个为0，就一定不在集合里）
2. 优点：空间效率和查询时间都远超过一般算法； 缺点：有一定误识别率和删除困难
3. 一般先布隆过滤器（不在就不需要继续），再看是否在数据库中才能判断在不在，案例：分布式系统，Redis缓存，垃圾邮件、评论等
4. python实现
   ```
      from bitarray import bitarray
      import mmh3

      class BloomFilter:
         def __init__(self,size,hash_num):
            self.size = size
            self.hash_num = hash_num
            self.bit_array = bitarray(size)
            self.bit_array.setall(0)
         def add(self,s):
            for seed in range(self.hash_num):
               result = mmh3.hash(s,seed) % self.size
               self.bit_array[result] = 1
         def lookup(self,s):
            for seed in range(self.hash_num):
               if self.bit_array[mmh3.hash(s,seed) % self.size] == 0: return 'Nope'
            return 'Probably'
      bf = BloomFilter(500000,7)
      bf.add('asdf')
      print(bf.lookup('asdf'))
      print(bf.lookup('qwer'))
   ```
