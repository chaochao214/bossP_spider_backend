//获取应用实例
const app = getApp()

Page({
  data: {
    search: {
      searchValue: '',
      showClearBtn: false
    },
    pageNum: 1,
    pageSize: 30,
    hasMoreData: true,
    searchResult: [],
    // items: []
  },
  onLoad: function (options) {
    // 页面初始化 options为页面跳转所带来的参数
  },
  onReady: function () {
    // 页面渲染完成
  },
  onShow: function () {
    // 页面显示
  },
  onHide: function () {
    // 页面隐藏
  },
  onUnload: function () {
    // 页面关闭
  },
  //输入内容时
  searchActiveChangeinput: function (e) {
    const val = e.detail.value;
    console.log(val);
    this.setData({
      'search.showClearBtn': val != '' ? true : false,
      'search.searchValue': val
    })
  },
  //点击清除搜索内容
  searchActiveChangeclear: function (e) {
    this.setData({
      'search.showClearBtn': false,
      'search.searchValue': ''
    })
  },
  //点击聚集时
  focusSearch: function () {
    console.log("--------------" + this.data.search.searchValue);
    if (this.data.search.searchValue != '') {
      this.setData({
        'search.showClearBtn': true
      })
    }
    console.log("--------------" + this.data.search.showClearBtn);
  },
  searchSubmit: function () {
    var that = this;
    that.setData({
      searchResult: [],
      hasMoreData: true,
      pageNum: 1
    })
    that.doSearch();
  },
  //搜索提交
  doSearch: function () {
    const val = this.data.search.searchValue;
    if (val) {
      const that = this
      wx.showToast({
        title: '搜索中',
        icon: 'loading'
      });
      wx.request({
        url: config.getFullurl("/getContentList"),
        data: {
          keyword: val,
          // pageNum: that.data.pageNum,
          // pageSize: that.data.pageSize
        },
        header: {
          'content-type': 'application/json',
        },
        method: 'GET', // OPTIONS, GET, HEAD, POST, PUT, DELETE, TRACE, CONNECT
        // header: {}, // 设置请求的 header
        success: function (res) {
          var contentlistTem = that.data.searchResult;
          if (res.data.status == 0) {
            if (that.data.pageNum == 1) {
              contentlistTem = []
            }
            var contentlist = res.data.data.pageData;
            console.log(that.data.pageNum);
            console.log(res.data.data);
            if (that.data.pageNum >= res.data.data.pageInfo.pageCount) {
              that.setData({
                searchResult: contentlistTem.concat(contentlist),
                hasMoreData: false,
                'search.showClearBtn': false
              })
            } else {
              that.setData({
                searchResult: contentlistTem.concat(contentlist),
                hasMoreData: true,
                pageNum: that.data.pageNum + 1,
                'search.showClearBtn': false,
              })
            }

          } else {
            wx.showToast({
              title: res.data.msg,
              success: function () {
                wx.redirectTo({
                  url: '../login/login',
                })
              }
            })
          }
        },
        fail: function () {
          // fail
          wx.showToast({
            title: '加载数据失败',
            icon: none
          })
        },
        complete: function () {
          // complete
          wx.hideToast();
        }
      })
    }
  },
  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    this.data.pageNum = 1
    this.doSearch()
  },
  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    if (this.data.hasMoreData) {
      this.doSearch()
    } else {
      wx.showToast({
        title: '没有更多数据',
      })
    }
  },


  // 搜索
  goSearch: function (e) {
    var that = this;
    that.setData({
      items: "",
    })
    var formData = e.detail.value;
    if (formData) {



      return new Promise((resolve, reject) => {
        wx.request({

          url: 'http://127.0.0.1:8000/bossP/search/' + formData,
          // data: {
          //   title: formData
          // },

          header: {
            'Content-Type': 'application/json'
          },
          success: function (res) {
            that.setData({
              items: res.data.data,
            })
            console.log(res.data)
            if (res.code == 1) {
              wx.showToast({
                title: '无相关搜索信息',
                icon: 'none',
                duration: 1500
              })
            } else {
              console.log(res.data.data)
              let str = JSON.stringify(res.data.data);
              console.log(str)
            }

            // console.log(res.data.msg)
          }
        })

      })

      wx.navigateTo({
        // url: '../searchShow/searchShow?data=' + str
        // url: '../searchShow/searchShow?data=' + res.data.data
        url: '../search/search'
      })
    } else {

      wx.showToast({
        title: '输入不能为空',
        icon: 'none',
        duration: 1500
      })

    }
  }

})