import math
# 請求書
class Invoice:
      def __init__ (self,invoiceNumber, invoiceDate, company, companyAddress, billToName, billToAddress, invoiceItemHeadNode):
            self.invoiceNumber = invoiceNumber;    # 請求書番号
            self.invoiceDate = invoiceDate     # 請求書を作成した日付
            self.company = company     # 会社名
            self.companyAddress = companyAddress   # 住所
            self.billToName = billToName       # 請求先の名前
            self.billToAddress = billToAddress # 請求先の住所
            self.invoiceItemHeadNode = invoiceItemHeadNode     # 購入したアイテムリストの開始を表す
    
      # 請求書の総額を計算
      def amountDue(self,taxes):
            currentNode = self.invoiceItemHeadNode
            total = 0
            while currentNode != None:
                  total += currentNode.getTotalPrice()
                  currentNode = currentNode.next

            if taxes == True:
                  return math.floor(total * 1.1)

            return total

      # 請求書の項目と数量を出力します。「item :shampoo, price :10, quantity:7」
      def printBuyingItems(self):
            print("Printing the Item List...")
            currentNode = self.invoiceItemHeadNode

            while currentNode != None:
                  print("item : " + currentNode.product.title + ", price : " + str(currentNode.product.price) + ", quantity: " + str(currentNode.quantity))
                  currentNode = currentNode.next

      # 請求書の詳細を返します。
      def printInvoice(self):

            print(
                  "Invoice\n" + 
                  "No. : " + self.invoiceNumber + 
                  "\nINVOICE DATE : " + self.invoiceDate + 
                  "\nSHIP TO : " + self.company + 
                  "\nADDRESS : " + self.companyAddress + 
                  "\nBILL TO : " + self.billToName + 
                  "\nADDRESS : " + self.billToAddress
            )

            # 各商品をprintしていきます
            currentNode = self.invoiceItemHeadNode
            while currentNode != None:
                  # f"{}"と書くことで、{}内に関数や変数を入れることができます。
                  print(f"{currentNode.product.title}(${str(currentNode.product.price)})--- {str(currentNode.quantity)} pcs. --- AMOUNT: {str(currentNode.product.price * currentNode.quantity)}")
                  currentNode = currentNode.next

            # 税抜きの合計額、税額、税込みの合計額
            subtotal = self.amountDue(False)
            print(f"SUBTOTAL : {subtotal}\nTax : {subtotal * 0.1}\nTOTAL : {subtotal * 1.1}")

# 製品の量
class InvoiceItemNode:
      def __init__ (self,quantity,product):
            self.quantity = quantity
            self.product = product
            self.next = None

      # 購入する数量に基づいて、製品の合計価格を計算
      def getTotalPrice(self):
            return self.quantity * self.product.price
    

# 製品
class Product:
      def __init__ (self,title, price):
            self.title =  title
            self.price = price


product1 = Product ("shampoo", 10)
product2 = Product ("conditioner", 5)
product3 = Product ("tooth brush", 3)

firstItem = InvoiceItemNode(7,product1)
secondItem = InvoiceItemNode(9,product2)
firstItem.next = secondItem
thirdItem = InvoiceItemNode(10,product3)
secondItem.next = thirdItem

invoice = Invoice ("UC1234567890", "2020/0506", "Recursion", "Los Angles", "Steven", "Dallas", firstItem)

invoice.printBuyingItems()
print(invoice.amountDue(False))
print(invoice.amountDue(True))