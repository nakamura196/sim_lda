<template>
    <footer class="footer"
            :class="{[`footer-${type}`]: type}"
            :data-background-color="backgroundColor">
        <div class="container">
            
            <nav>
            </nav>
            <div class="copyright">
                地域文化資源デジタルアーカイブ
                <hr/>
                Design from <a href="https://www.creative-tim.com/">Creative Tim</a>.
            </div>
        </div>
    </footer>
</template>
<script>
export default {
  props: {
    backgroundColor: String,
    type: String
  },
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>
<style>
</style>
