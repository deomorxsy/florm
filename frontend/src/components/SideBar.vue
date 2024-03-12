<!-- Sidebar.vue -->

<template>
<nav id="sidebar">
     <!--<img src="src/images/avatar.jpg" id="user_avatar" alt="Avatar">-->
     <!-- Sidebar with conditional class based on isSidebarHidden -->
     <aside class="sidebar" :class="{ 'sidebar-hidden': isSidebarHidden }">
        <div id="sidebar_content">
            <div id="user">
                <p id="user_infos">
                    <span class="item-description">
                        Username area
                    </span>
                    <span class="item-description">
                        Lorem Ipsum
                    </span>
                </p>
            </div>

            <ul id="side_items">
                <li class="side-item active">
                    <a href="#">
                        <i class="fa-solid fa-chart-line"></i>
                        <span class="item-description">
                            Dashboard
                        </span>
                    </a>
                </li>

                <li class="side-item">
                    <a href="#">
                        <i class="fa-solid fa-user"></i>
                        <span class="item-description">
                            Usuários
                        </span>
                    </a>
                </li>

                <li class="side-item">
                    <a href="#">
                        <i class="fa-solid fa-box"></i>
                        <span class="item-description">
                            Profile
                        </span>
                    </a>
                </li>

                <li class="side-item">
                    <a href="#">
                        <i class="fa-solid fa-gear"></i>
                        <span class="item-description">
                            About
                        </span>
                    </a>
                </li>
            </ul>
            <button id="open_btn" @click="toggleSidebar" class="toggle-btn">
                <i id="open_btn_icon" class="fa-solid fa-chevron-right">
                    {{ sidebarButton }}
                </i>
            </button>
        </div>

        <div id="logout">
            <button id="logout_btn">
                <i class="fa-solid fa-right-from-bracket"></i>
                <span class="item-description">
                     Logout
                </span>
            </button>

        </div>
     </aside>
    </nav>
</template>

<script>
export default {
  name: 'Sidebar',
  data() {
    return {
      isSidebarHidden: false,
      sidebarButton: '<',
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarHidden = !this.isSidebarHidden;
      if (this.sidebarButton == '>') {
          this.sidebarButton = '<';
      } else {
          this.sidebarButton = '>';
      }
    },
  },
};
</script>

<style scoped>

.sidebar {
  width: 200px;
  height: 100%;
  background-color: #333;
  color: white;
  padding: 20px;
  transition: margin-left 0.3s;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  overflow-x: hidden;
  transition: 0.5s;
  padding-top: 60px;
}


/*#sidebar {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    background-color: #ffffff;
    height: 100vh;
    border-radius: 0px 18px 18px 0px;
    position: relative;
    transition: all .5s;
    min-width: 82px;
    z-index: 2;
}*/

#sidebar_content {
    padding: 12px;
}


.sidebar-hidden {
  margin-left: -200px;
}

.toggle-btn {
  position: fixed; /* or use 'absolute' depending on your layout */
  top: 50px; /* adjust the position as needed */
  left: 200px; /* adjust the position as needed */
  background-color: #444;
  color: white;
  padding: 5px;
  border: none;
  cursor: pointer;
}

#open_btn {
    font-size: 40px;
    position: absolute;
    top: 30px;
    right: -10px;
    padding: 20px;
}

#Logout {
    border-top: 1px solid #e3e9f7;
    padding: 12px;
    background: red;
}

#Logout_btn {
    border: none;
    padding: 12px;
    font-size: 14;
    display: flex;
    gap: 20px;
    align-items: center;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

a {
  color: white;
  text-decoration: none;
}
</style>

