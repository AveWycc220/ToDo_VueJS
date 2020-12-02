class Api {
  static async getData({name=undefined, login=true}) {
    let url = ''
    if (login) {
      url = `http://${process.env.VUE_APP_SERVER_DOMAIN}:${process.env.VUE_APP_SERVER_PORT}/login/${name}.json`
    } else {
      url = `http://${process.env.VUE_APP_SERVER_DOMAIN}:${process.env.VUE_APP_SERVER_PORT}/get`
    }
    console.log(`Connect to ${url}`)
    try {
      let res = await fetch(url, {
        method: 'GET',
        mode: 'cors',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': 'Bearer ' + process.env.VUE_APP_TOKEN,
        }
      })
      if (res.ok) {
        if (login) {
          return res.status
        } else {
          return res.json()
        }
      } else {
        return res.status
      }
    } catch (e) {
      console.log(`Error! ${e}`)
    }
    return false;
  }
}

export default Api